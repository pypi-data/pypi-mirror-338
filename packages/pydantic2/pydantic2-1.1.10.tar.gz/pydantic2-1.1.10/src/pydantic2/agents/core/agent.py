"""Form agent for handling form processing."""

import json
# import logging # Removed unused import
from typing import Dict, Any, Optional, Type, List
import traceback

from ..models.form import FormData, BaseFormModel
from ..models.analytics import AnalyticsResult
from ..providers.openrouter import OpenRouterProvider
from ..utils.logging_config import SimpleLogger


class FormAgent:
    """
    Agent responsible for processing user messages, extracting form data,
    and generating analytics based on the completed form.
    It interacts directly with an LLM provider.
    """

    def __init__(
        self,
        api_key: str,
        model_name: str = "openai/gpt-4o-mini",
        temperature: float = 0.1,
    ):
        """
        Initializes the FormAgent.

        Args:
            api_key: API key for the LLM provider.
            model_name: Name of the LLM model to use.
            temperature: Default sampling temperature for LLM generations.
        """

        self.logger = SimpleLogger("core.agent")
        self.temperature = temperature

        # Initialize provider
        try:
            self.provider = OpenRouterProvider(
                api_key=api_key,
                model_name=model_name
            )
            self.logger.info(f"Initialized FormAgent with model {model_name}")
        except Exception as e:
            self.logger.error(f"Failed to initialize LLM provider: {e}")
            raise ValueError(f"Failed to initialize LLM provider: {str(e)}")

    async def process_message(
        self,
        message: str,
        form_data: FormData,
        form_class: Type[BaseFormModel],
        message_history: Optional[List[Dict[str, Any]]] = None,
        role_prompt: str = ""
    ) -> FormData:
        """
        Processes a user message, updates the form data, and potentially generates analytics.

        Args:
            message: The user's message content.
            form_data: The current state of the form data (including metadata and system config).
            form_class: The Pydantic model class representing the form structure.
            message_history: A list of previous messages in the conversation.
            role_prompt: An additional prompt defining the specific role for the LLM.

        Returns:
            The updated FormData object.
        """
        # Use form_data.system.completion_achieved property
        if form_data.system.completion_achieved:
            # Form threshold reached, generate analytics (if not already generated)
            if form_data.analytics is None:
                self.logger.info("Completion threshold reached. Generating analytics.")  # Log info
                return await self._generate_analytics(message, form_data, form_class, message_history or [])
            else:
                # Analytics already exist, just return current state (or handle differently?)
                # TODO: Decide how to handle messages arriving after analytics generation.
                # For now, just log and return form_data without applying the message to the form itself.
                self.logger.info("Form already complete and analytics generated. Ignoring further message for form filling.")  # Log info directly
                # Update history and return
                form_data.metadata.history.append(message)
                return form_data
        else:
            # Form not yet complete, extract information
            self.logger.info("Extracting form information from message.")  # Log info
            return await self._extract_form_info(message, form_data, form_class, message_history or [], role_prompt)

    async def _extract_form_info(
        self,
        message: str,
        form_data: FormData,
        form_class: Type[BaseFormModel],
        message_history: List[Dict[str, Any]],
        role_prompt: str = ""
    ) -> FormData:
        """
        Extract information from user message and update form.

        Args:
            message: User message
            form_data: Current form data
            form_class: Form class
            message_history: Message history
            role_prompt: Additional prompt text for role customization

        Returns:
            Updated form data
        """
        try:
            self.logger.debug("Agent: Entering _extract_form_info")

            # Get form schema for form illustration
            form_schema = form_class.model_json_schema()

            # Get current form data dump
            self.logger.debug("Agent: Attempting to dump current form data...")
            current_user_form = form_data.user_form.model_dump() if hasattr(form_data.user_form, "model_dump") else {}
            self.logger.debug("Agent: Current form data dumped successfully.")

            # Prepare prompt for information extraction
            self.logger.debug("Agent: Preparing system message...")
            system_message = f"""
            You are a form processing assistant. Your job is to:
            1. Extract relevant information from user messages to fill form fields
            2. Update the form data with extracted information
            3. Calculate the completion progress (0-100%)
               - Don't decrease the progress.
            4. Generate the next question to ask the user
            5. Detect the user's language

            [REQUIREMENTS]
            - Be very friendly and engaging.
            - If user didn't provide any information, just remind him what information you need.
            - Use the same language as the user in your responses.
            - {role_prompt}
            [/REQUIREMENTS]
            """
            self.logger.debug("Agent: System message prepared.")

            self.logger.debug("Agent: Preparing prompt string...")
            prompt = f"""
            CURRENT_PROGRESS:
            {form_data.metadata.progress}%

            [USER_MESSAGE]
            {message}
            [/USER_MESSAGE]

            [FORM_SCHEMA]
            {json.dumps(form_schema, indent=2, ensure_ascii=False)}
            [/FORM_SCHEMA]

            [CURRENT_FORM_DATA]
            {json.dumps(current_user_form, indent=2, ensure_ascii=False)}
            [/CURRENT_FORM_DATA]

            [MESSAGE_HISTORY]
            {json.dumps(message_history[-5:] if message_history else [], indent=2, ensure_ascii=False)}
            [/MESSAGE_HISTORY]

            Analyze the [USER_MESSAGE] and extract information to improve the form data.

            The 'next_message_ai' field:
            - If user asking for help, just respond with a message that you're here to help and ask them to rephrase their message.
            - If user providing information, congratulate them for providing the information and ask the question that you need.
            - If user didn't provide any information, just remind him what information you need.
            - Continue asking questions until the form is complete, especially for required fields.
            - Use same language that user is using in their message.

            User form requirements:
            - Improve the information in the form data based on the [USER_MESSAGE] and [CURRENT_FORM_DATA].
            - Correct and rephrase the information for more accuracy.
            - If you're not sure about a form field value, don't include it in the response.

            Return a valid JSON object with the following fields:
            - form_data: object with extracted form values (matching the form schema)
            - progress: number from 0-100 indicating completion percentage
            - next_message_ai: next message to send to the user
            - user_language: detected user language code (e.g., "en", "ru", "es")
            """
            self.logger.debug("Agent: Prompt string prepared.")

            # Get response from LLM
            self.logger.info("Agent: Calling LLM provider for form info extraction...")
            response = await self.provider.json_completion(
                prompt=prompt,
                system_message=system_message,
                temperature=self.temperature
            )
            self.logger.info("Agent: Received response from LLM provider")

            # Extract response as JSON
            response_json = response if isinstance(response, dict) else {}
            self.logger.debug(f"Agent: Received LLM response JSON: {json.dumps(response_json, indent=2, ensure_ascii=False)}")

            if not response_json:
                self.logger.error("Empty response from LLM during form info extraction")
                return self._create_error_response(form_data, "I encountered an error processing your information.")

            # Check if response_json is already in form format (direct fields) instead of wrapped format
            # If it contains typical form fields but no form_data key, treat it as the form data directly
            if ("name" in response_json or "industry" in response_json) and "form_data" not in response_json:
                self.logger.debug("Agent: LLM returned form data directly, not wrapped in 'form_data'")
                form_updates = response_json  # Use the response directly as form data
            else:
                # Extract form_data normally
                form_updates = response_json.get("form_data")  # <<< Get update data

            # Update form data if we have updates
            if form_updates:
                # Log the data being used to update the form at DEBUG level
                self.logger.debug(f"Agent: Attempting to update form with: {json.dumps(form_updates, indent=2, ensure_ascii=False)}")
                form_data.update_form(form_updates)
            else:
                self.logger.debug("Agent: No form data updates found in LLM response")  # <<< Log if no update data

            # Get progress and ensure it's an integer
            # Log the progress value obtained from the response (or default) at DEBUG level
            progress_from_llm = response_json.get("progress")  # <<< Get progress value
            self.logger.debug(f"Agent: Progress value directly from LLM response: {progress_from_llm}")  # <<< Log raw progress
            progress = progress_from_llm if progress_from_llm is not None else form_data.metadata.progress
            self.logger.debug(f"Agent: Progress value to use (after default): {progress}")  # <<< Log final progress value

            if isinstance(progress, float):
                self.logger.debug(f"Agent: Converting float progress {progress} to int.")
                progress = int(progress)
            elif not isinstance(progress, int):
                self.logger.warning(f"Agent: Progress value is not int or float ({type(progress)}): {progress}. Defaulting to current progress: {form_data.metadata.progress}")
                progress = form_data.metadata.progress  # Fallback safely

            # Update metadata and completion status using the new method
            form_data.update_progress(progress)  # Updates self.metadata.progress & self.system.completion_achieved
            form_data.metadata.next_message_ai = response_json.get("next_message_ai", "What else would you like to share?")
            form_data.metadata.history.append(message)  # Append original user message
            form_data.metadata.user_language = response_json.get("user_language", form_data.metadata.user_language)

            self.logger.info(f"Form info extracted. Progress: {form_data.metadata.progress}%")
            return form_data

        except Exception as e:
            self.logger.error(f"Error extracting form info: {e}")
            self.logger.error(traceback.format_exc())
            return self._create_error_response(form_data, "I encountered an error processing your information.")

    async def _generate_analytics(
        self,
        message: str,
        form_data: FormData,
        form_class: Type[BaseFormModel],
        message_history: List[Dict[str, Any]]
    ) -> FormData:
        """
        Generate analytics based on the completed form.

        Args:
            message: User message
            form_data: Current form data
            form_class: Form class
            message_history: Message history

        Returns:
            Updated form data with analytics
        """
        try:
            # Get the latest form data from the database
            session_id = form_data.system.session_id
            if session_id:
                self.logger.info(f"Agent: Getting latest form data from DB for session {session_id}")
                # Import SessionManager here to avoid circular imports
                from .session import SessionManager

                # Create SessionManager instance to access the database
                session_manager = SessionManager()

                # Get the latest form state from the database
                latest_form_data_dict = await session_manager.get_latest_form_data(session_id)

                if latest_form_data_dict:
                    self.logger.info("Agent: Successfully retrieved latest form data from DB")

                    # Extract only the form data from the retrieved dictionary
                    latest_user_form_data = latest_form_data_dict.get("user_form", {})

                    if latest_user_form_data:
                        self.logger.info(f"Agent: Found user_form data in DB: {json.dumps(latest_user_form_data, indent=2, ensure_ascii=False)}")

                        # Update the form with the retrieved data
                        form_data.update_form(latest_user_form_data)
                        self.logger.info("Agent: Updated form with data from DB")
                    else:
                        self.logger.warning("Agent: DB record found but no user_form data in it")
                else:
                    self.logger.warning(f"Agent: No form data found in DB for session {session_id}")
            else:
                self.logger.warning("Agent: No session_id available, cannot retrieve form from DB")

            # Before getting data, output information about what we have at the start
            self.logger.debug(f"Agent: Starting analytics generation... Current form fields: {form_data.user_form.model_fields_set if hasattr(form_data.user_form, 'model_fields_set') else 'unknown'}")

            # Save a copy of the entire FormData structure before working with it
            # Try different ways to save data to ensure its safety
            current_user_form_dump = form_data.user_form.model_dump() if hasattr(form_data.user_form, "model_dump") else {}

            # Save the original form data for debugging
            self.logger.debug(f"Agent: Original form data: {json.dumps(current_user_form_dump, indent=2, ensure_ascii=False)}")

            # Additionally save form attributes in a simple way as a backup
            original_form_attrs = {}
            for attr_name in dir(form_data.user_form):
                if not attr_name.startswith('_') and not callable(getattr(form_data.user_form, attr_name)):
                    try:
                        original_form_attrs[attr_name] = getattr(form_data.user_form, attr_name)
                    except Exception:
                        pass

            self.logger.debug(f"Agent: Original form attributes: {original_form_attrs}")

            # Prepare system message for analytics
            system_message = """

            You are a data analysis assistant. Your task is to provide comprehensive insights based on submitted form data and user interaction history.

            Return ONLY a valid JSON object conforming exactly to the following JSON Schema.

            Do NOT include any other text or explanations outside the JSON object itself:
            [SCHEMA]
            {schema}
            [/SCHEMA]
            """

            analytics_schema = AnalyticsResult.model_json_schema()
            system_message = system_message.format(schema=json.dumps(analytics_schema, indent=2, ensure_ascii=False))

            # Prepare prompt for analytics generation
            prompt = f"""
            [FORM_DATA_TO_ANALYZE]
            {json.dumps(current_user_form_dump, indent=2, ensure_ascii=False)}
            [/FORM_DATA_TO_ANALYZE]

            [LAST_USER_MESSAGE]
            {message}
            [/LAST_USER_MESSAGE]

            [CONVERSATION_HISTORY]
            {json.dumps(message_history[-10:] if message_history else [], indent=2, ensure_ascii=False)} # Use a bit more history for user analysis
            [/CONVERSATION_HISTORY]

            Based on the Form Data, Last User Message, and Conversation History, perform the analysis tasks described in the system message.
            Return the complete analysis as a JSON object matching the [SCHEMA] provided.
            Focus on providing objective assessments for both data quality and user analysis.
            """

            # Get response from LLM
            response = await self.provider.json_completion(
                prompt=prompt,
                system_message=system_message,
                temperature=self.temperature * 1.2  # Slightly higher temperature for creative analysis
            )

            # Log response
            self.logger.info(f"Agent: LLM response for analytics: {json.dumps(response, indent=2, ensure_ascii=False)}")

            # Extract response as JSON
            response_json = response if isinstance(response, dict) else {}

            if not response_json:
                self.logger.error("Empty response from LLM during analytics generation")
                return self._create_error_response(form_data, "I encountered an error analyzing your information.")

            # Validate analytics data
            try:
                analytics_data = AnalyticsResult.model_validate(response_json)
                self.logger.info(f"Agent: Validated analytics data: {json.dumps(analytics_data.model_dump(), indent=2, ensure_ascii=False)}")
            except Exception as validation_error:
                self.logger.error(f"Analytics response validation failed: {validation_error}")
                # Use empty analytics as fallback
                analytics_data = AnalyticsResult.create_empty()

            # ----------- SAVE FORM DATA --------------
            # Option 1: Create a completely new form instance from original data
            new_form_instance = form_class.model_validate(current_user_form_dump)

            # Compare fields for debugging
            if hasattr(new_form_instance, 'model_dump'):
                new_form_dump = new_form_instance.model_dump()
                self.logger.debug(f"Agent: New form instance data: {json.dumps(new_form_dump, indent=2, ensure_ascii=False)}")

                # Check for mismatches between original and new form
                if current_user_form_dump != new_form_dump:
                    self.logger.warning("Agent: New form instance differs from original data!")
                    # Identify mismatched fields
                    for key in set(current_user_form_dump.keys()) | set(new_form_dump.keys()):
                        if key not in current_user_form_dump:
                            self.logger.warning(f"Agent: Key {key} missing in original data")
                        elif key not in new_form_dump:
                            self.logger.warning(f"Agent: Key {key} missing in new form")
                        elif current_user_form_dump[key] != new_form_dump[key]:
                            self.logger.warning(f"Agent: Value for {key} differs: original={current_user_form_dump[key]}, new={new_form_dump[key]}")

            # Option 2: Update existing form field
            if current_user_form_dump:
                # Update form_data.user_form with data from current_user_form_dump
                form_data.update_form(current_user_form_dump)
                self.logger.debug(f"Agent: After update_form, form data is: {json.dumps(form_data.user_form.model_dump() if hasattr(form_data.user_form, 'model_dump') else {}, indent=2, ensure_ascii=False)}")

            # Option 3: Set new form instance directly
            # Replace user_form with new instance only if data in current form is empty
            # This is insurance in case previous methods didn't work
            if hasattr(form_data.user_form, 'model_dump') and not any(form_data.user_form.model_dump().values()):
                self.logger.warning("Agent: Current form data is empty, replacing with new instance")
                form_data.user_form = new_form_instance
            # ----------- END SAVE FORM DATA --------------

            # Update metadata
            form_data.update_progress(100)  # Always set progress to 100 for completed analytics
            form_data.metadata.next_message_ai = "Here is my analysis of your information."
            form_data.metadata.history.append(message)

            # Save analytics to FormData directly (not in metadata)
            form_data.analytics = analytics_data

            # Final check before return
            if hasattr(form_data.user_form, 'model_dump'):
                final_form_dump = form_data.user_form.model_dump()
                self.logger.debug(f"Agent: Final form data before return: {json.dumps(final_form_dump, indent=2, ensure_ascii=False)}")

                # If form is empty, restore from original once more
                if not any(final_form_dump.values()) and current_user_form_dump:
                    self.logger.warning("Agent: Final form is still empty, forcing restore from original")
                    form_data.user_form = new_form_instance

            self.logger.info(f"Generated analytics for form: {form_data.user_form.__class__.__name__}")
            return form_data

        except Exception as e:
            self.logger.error(f"Error generating analytics: {e}")
            self.logger.error(traceback.format_exc())
            return self._create_error_response(form_data, "I encountered an error analyzing your information.")

    def _create_error_response(self, form_data: FormData, error_message: str) -> FormData:
        """Creates a generic error response to send back to the processor."""
        self.logger.warning(f"Creating error response: {error_message}")  # Log warning
        form_data.metadata.next_message_ai = "Could you try rephrasing your last message?"
        # Potentially reset progress or add specific error metadata here if needed
        return form_data
