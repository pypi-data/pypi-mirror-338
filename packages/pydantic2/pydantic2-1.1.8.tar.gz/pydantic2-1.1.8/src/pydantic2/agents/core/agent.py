"""Form agent for handling form processing."""

import json
import logging
from typing import Dict, Any, Optional, Type, List

from ..models.form import FormData, BaseFormModel
from ..models.analytics import AnalyticsResult
from ..providers.openrouter import OpenRouterProvider

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("core.agent")


class FormAgent:
    """
    Agent for form processing and analysis.

    This class handles the processing of user messages, form data extraction,
    and analytics generation. It uses a direct approach with LLM calls
    rather than an agent framework to avoid validation errors.
    """

    def __init__(
        self,
        api_key: str,
        model_name: str = "openai/gpt-4o-mini",
        temperature: float = 0.1,
        verbose: bool = False
    ):
        """
        Initialize form agent.

        Args:
            api_key: API key for LLM provider
            model_name: Model name to use
            temperature: Default temperature for generations
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        self.temperature = temperature

        # Initialize provider
        try:
            self.provider = OpenRouterProvider(
                api_key=api_key,
                model_name=model_name
            )
            logger.info(f"Initialized FormAgent with model {model_name}")
        except Exception as e:
            logger.error(f"Failed to initialize LLM provider: {e}")
            raise ValueError(f"Failed to initialize LLM provider: {str(e)}")

    async def process_message(
        self,
        message: str,
        form_data: FormData,
        form_class: Type[BaseFormModel],
        message_history: Optional[List[Dict[str, Any]]] = None
    ) -> FormData:
        """
        Process a user message and update form data.

        Args:
            message: User message
            form_data: Current form data
            form_class: Form class
            message_history: Message history

        Returns:
            Updated form data
        """
        # Пороговое значение прогресса для запуска аналитики
        ANALYTICS_THRESHOLD = 65

        if form_data.is_complete() or form_data.metadata.progress >= ANALYTICS_THRESHOLD:
            # Форма завершена или прогресс достаточно высок, генерируем аналитику
            return await self._generate_analytics(message, form_data, form_class, message_history or [])
        else:
            # Форма не завершена, извлекаем информацию
            return await self._extract_form_info(message, form_data, form_class, message_history or [])

    async def _extract_form_info(
        self,
        message: str,
        form_data: FormData,
        form_class: Type[BaseFormModel],
        message_history: List[Dict[str, Any]]
    ) -> FormData:
        """
        Extract information from user message and update form.

        Args:
            message: User message
            form_data: Current form data
            form_class: Form class
            message_history: Message history

        Returns:
            Updated form data
        """
        try:
            # Get form schema and current data
            form_schema = form_class.model_json_schema()
            current_form_data = form_data.form.model_dump() if hasattr(form_data.form, "model_dump") else {}

            # Prepare prompt for information extraction
            system_message = """
            You are a form processing assistant. Your job is to:
            1. Extract relevant information from user messages to fill form fields
            2. Update the form data with extracted information
            3. Calculate the completion progress (0-100%)
            4. Generate the next question to ask the user
            5. Respond to the user's message
            """

            prompt = f"""
            # User Message
            {message}

            # Form Schema
            {json.dumps(form_schema, indent=2)}

            # Current Form Data
            {json.dumps(current_form_data, indent=2)}

            # Current Progress
            {form_data.metadata.progress}%

            # Message History
            {json.dumps(message_history[-5:] if message_history else [], indent=2)}

            Analyze the user message and update the form data.

            Return a JSON object with the following fields:
            - form_data: object with extracted form values
            - progress: number from 0-100 indicating completion percentage
            - message: response to the user
            - next_message_ai: next message to send to the user
            - user_language: detected user language code (e.g., "en", "ru", "es")

            Requirements:
            - Be very friendly and engaging.
            - If user didn't provide any information, just remind him what information you need.

            The 'next_message_ai' field:
            - If user asking for help, just respond with a message that you're here to help and ask them to rephrase their message.
            - If user providing information, congratulate them for providing the information and ask the question that you need.
            - If user didn't provide any information, just remind him what information you need.
            - Continue asking questions until the form is complete, especially for required fields.
            - Use same language that user is using in their message.
            -If you're not sure about a form field value, don't include it in form_data.

            Form requirements:
            - Improve the information in 'form_data' field.
            - Correct and rephrase the information for more accuracy.
            - If you're not sure about a form field value, don't include it in form_data.
            """

            # Get response from LLM
            response = await self.provider.json_completion(
                prompt=prompt,
                system_message=system_message,
                temperature=self.temperature
            )

            # Extract response as JSON
            response_json = response if isinstance(response, dict) else {}

            if not response_json:
                logger.error("Empty response from LLM")
                return self._create_error_response(form_data, "I encountered an error processing your information.")

            # Update form data
            if "form_data" in response_json and response_json["form_data"]:
                form_data.update_form(response_json["form_data"])

            # Get progress and ensure it's an integer
            progress = response_json.get("progress", form_data.metadata.progress)
            if isinstance(progress, float):
                progress = int(progress)

            # Update metadata
            form_data.metadata.next_message_ai = response_json.get("next_message_ai", "What else would you like to share?")
            form_data.metadata.progress = progress
            form_data.metadata.history.append(message)
            form_data.metadata.user_language = response_json.get("user_language", form_data.metadata.user_language)

            # Check if form is now complete
            if form_data.metadata.progress >= 100:
                form_data.metadata.completion_achieved = True
                form_data.metadata.next_message_ai = "Would you like a detailed analysis of your information?"

            return form_data

        except Exception as e:
            logger.error(f"Error extracting form info: {e}")
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
            # Prepare form data for analytics
            current_form_data = form_data.form.model_dump() if hasattr(form_data.form, "model_dump") else {}

            # Prepare prompt for analytics generation
            system_message = """
            You are an analytics assistant that provides insights based on form data.
            Analyze the form data and generate detailed insights, recommendations, and a SWOT analysis.

            Return a valid JSON object with these fields:
            - analysis: detailed analysis of the form data
            - recommendations: list of actionable recommendations
            - strengths: list of identified strengths
            - weaknesses: list of identified weaknesses
            - opportunities: list of identified opportunities
            - risks: list of identified risks
            - score: numerical score from 0-10
            - next_steps: list of suggested next steps
            - message: summary message to the user
            """

            prompt = f"""
            # Form Data
            {json.dumps(current_form_data, indent=2)}

            # User Message
            {message}

            # Message History
            {json.dumps(message_history[-5:] if message_history else [], indent=2)}

            Analyze the form data and provide detailed insights and recommendations.
            Return a JSON object with the fields described in the system message.
            """

            # Get response from LLM
            response = await self.provider.json_completion(
                prompt=prompt,
                system_message=system_message,
                temperature=self.temperature * 1.2  # Slightly higher temperature for creative analysis
            )

            # Extract response as JSON
            response_json = response if isinstance(response, dict) else {}

            if not response_json:
                logger.error("Empty response from LLM")
                return self._create_error_response(form_data, "I encountered an error analyzing your information.")

            # Validate analytics data
            analytics_data = AnalyticsResult.model_validate(response_json)

            # Ensure progress is 100 and an integer (convert if it's a float)
            progress = 100
            if isinstance(progress, float):
                progress = int(progress)

            # Update metadata
            form_data.metadata.next_message_ai = response_json.get("message", "Here is my analysis of your information.")
            form_data.metadata.history.append(message)
            form_data.metadata.progress = progress
            form_data.metadata.completion_achieved = True

            # Важно: сохраняем аналитику в метаданных
            form_data.metadata.analytics = analytics_data

            logger.info(f"Generated analytics for form: {form_data.form.__class__.__name__}")
            return form_data

        except Exception as e:
            logger.error(f"Error generating analytics: {e}")
            return self._create_error_response(form_data, "I encountered an error analyzing your information.")

    def _create_error_response(self, form_data: FormData, error_message: str) -> FormData:
        """Create an error response when something goes wrong."""
        form_data.metadata.next_message_ai = "Could you try rephrasing your last message?"
        return form_data
