"""Form processor for handling user interaction."""

# import logging # Removed unused import
import traceback
from typing import Dict, Any, Optional, Type

from pydantic import BaseModel

from ..models.form import FormData, BaseFormModel, FormMetadata, System, SessionInfo
from ..models.analytics import AnalyticsResult
from .agent import FormAgent
from .session import SessionManager
from ..utils.logging_config import SimpleLogger
from ..utils.text_sanitizer import sanitize_text


class FormProcessor:
    """
    Main entry point for form processing.

    This class ties together the form agent and session manager
    to provide a complete form processing solution.
    """

    def __init__(
        self,
        form_class: Type[BaseFormModel],
        api_key: str,
        role_prompt: str,
        model_name: str = "openai/gpt-4o-mini",
        temperature: float = 0.1,
        db_path: Optional[str] = None,
        client_id: str = "default",
        completion_threshold: int = 100,
        verbose: bool = False
    ):
        """
        Initializes the FormProcessor.

        Args:
            form_class: The Pydantic model class defining the form structure.
            api_key: The API key for the LLM provider.
            role_prompt: An additional prompt defining the LLM's specific role during processing.
            model_name: The name of the LLM model to use.
            temperature: The sampling temperature for LLM generation.
            db_path: Optional path to the SQLite database file for session persistence.
            client_id: An identifier for the client application.
            completion_threshold: The progress percentage required to consider the form complete.
        """

        SimpleLogger.set_agents_logs_visible(verbose)

        # Create a logger for this class
        self.logger = SimpleLogger("core.processor")

        self.form_class = form_class
        self.client_id = client_id
        self.completion_threshold = completion_threshold
        self.role_prompt = role_prompt
        self.model_name = model_name  # Store model_name
        self.temperature = temperature  # Store temperature

        self.logger.info(f"FormProcessor initialized with completion_threshold: {self.completion_threshold}")

        # Validate inputs
        if not api_key:
            self.logger.error("API key is required")  # Log error directly
            raise ValueError("API key is required")

        if not issubclass(form_class, BaseModel):
            self.logger.error("Form class must be a subclass of BaseModel")  # Log error directly
            raise ValueError("Form class must be a subclass of BaseModel")

        try:
            self.agent = FormAgent(
                api_key=api_key,
                model_name=model_name,
                temperature=temperature,
            )
            self.logger.info(f"Form agent initialized with model {model_name}")  # Log info directly
        except Exception as e:
            self.logger.error(f"Failed to initialize form agent: {e}")
            raise ValueError(f"Failed to initialize form agent: {str(e)}")

        try:
            self.session_manager = SessionManager(
                db_path=db_path,
            )
            self.logger.info("Session manager initialized")  # Log info directly
        except Exception as e:
            self.logger.error(f"Failed to initialize session manager: {e}")
            raise ValueError(f"Failed to initialize session manager: {str(e)}")

    async def start_session(self, user_id: str) -> str:
        """
        Starts a new form processing session for a given user.

        Args:
            user_id: The unique identifier for the user.

        Returns:
            The newly created session identifier.
        """
        try:
            # Create a new session
            session_id = await self.session_manager.create_session(
                user_id=user_id,
                client_id=self.client_id,
                form_class=self.form_class.__name__
            )

            # Create empty form data with system config
            # Populate System model with session context
            system_config = System(
                completion_threshold=self.completion_threshold,
                completion_achieved=False,  # Initial state
                session_id=session_id,
                client_id=self.client_id,
                role_prompt=self.role_prompt,
                model_name=self.model_name,
                temperature=self.temperature,
                form_defaults=self.form_class().model_dump()
            )

            # Create SessionInfo with empty form
            session_info = SessionInfo(
                user_form=self.form_class()
            )

            # Create FormData with session_info and system config
            form_data = FormData(
                session_info=session_info,
                system=system_config  # Use the populated system config
            )

            # Save initial form data
            await self.session_manager.save_form_data(form_data, session_id)

            # Save welcome message
            await self.session_manager.save_message(
                role="assistant",
                content=form_data.session_info.metadata.next_message_ai,
                session_id=session_id
            )

            self.logger.info(f"Started new session: {session_id}")  # Log info directly
            return session_id

        except Exception as e:
            self.logger.error(f"Error starting session: {e}")
            self.logger.error(traceback.format_exc())
            raise ValueError(f"Failed to start session: {str(e)}")

    async def process_message(
        self,
        message: str,
        session_id: str
    ) -> FormData:
        """
        Processes a user message within a specific session, updating the form state.

        Args:
            message: The user's message content.
            session_id: The identifier of the session to process the message in.

        Returns:
            The updated FormData object reflecting the changes after processing the message.
        """
        if not session_id:
            self.logger.error("Session ID is required in process_message")  # Log error
            raise ValueError("Session ID is required")

        # Sanitize user input
        sanitized_message = sanitize_text(message)
        if message != sanitized_message:
            self.logger.info(f"Original message sanitized. Original: '{message}', Sanitized: '{sanitized_message}'")  # Log info

        try:
            # Set current session
            self.session_manager.session_id = session_id

            # Get session info to verify session exists
            session_info = await self.session_manager.get_session_info(session_id)
            if not session_info:
                self.logger.error(f"Session not found: {session_id}")  # Log error
                raise ValueError(f"Session not found: {session_id}")

            # Get message history
            message_history = await self.session_manager.get_messages(session_id)

            # Save sanitized user message
            await self.session_manager.save_message(
                role="user",
                content=sanitized_message,  # Save sanitized message
                session_id=session_id
            )

            # Get latest form data
            form_data_dict: Dict[str, Any] | None = await self.session_manager.get_latest_form_data(session_id)
            self.logger.info(f"Loaded form data dict from DB: {form_data_dict}")  # Log info directly
            if not form_data_dict:
                self.logger.warning(f"No form data found for session {session_id}, creating empty")  # Log warning directly
                form_data = FormData(
                    session_info=SessionInfo(
                        user_form=self.form_class(),
                        metadata=FormMetadata()
                    ),
                    system=System(completion_threshold=self.completion_threshold)
                )
            else:
                try:
                    # Reconstruct form data from dict, including system config
                    form_instance = self.form_class.model_construct(
                        **form_data_dict.get("user_form", {})
                    )
                    metadata_dict = form_data_dict.get("metadata", {})
                    system_dict = form_data_dict.get("system", {})
                    analytics_dict = form_data_dict.get("analytics")

                    analytics_obj = None
                    if analytics_dict:
                        try:
                            analytics_obj = AnalyticsResult.model_validate(analytics_dict)
                        except Exception as analytics_exc:
                            self.logger.error(f"Error reconstructing analytics in process_message: {analytics_exc}")

                    # Create session_info first
                    session_info = SessionInfo(
                        user_form=form_instance,
                        metadata=FormMetadata.model_validate(metadata_dict)
                    )

                    # Create FormData with session_info
                    form_data = FormData(
                        session_info=session_info,
                        system=System.model_validate(system_dict),
                        analytics=analytics_obj
                    )
                except Exception as e:
                    self.logger.error(f"Error reconstructing form data: {e}")
                    # Fallback to empty form data with system config
                    form_data = FormData(
                        session_info=SessionInfo(
                            user_form=self.form_class(),
                            metadata=FormMetadata()
                        ),
                        system=System(completion_threshold=self.completion_threshold)
                    )

            # Process sanitized message with agent
            updated_form_data = await self.agent.process_message(
                message=sanitized_message,  # Use sanitized message
                form_data=form_data,
                form_class=self.form_class,
                message_history=message_history,
                role_prompt=self.role_prompt
            )

            # Save assistant message
            await self.session_manager.save_message(
                role="assistant",
                content=updated_form_data.session_info.metadata.next_message_ai,
                session_id=session_id
            )

            # Save updated form data
            await self.session_manager.save_form_data(
                form_data=updated_form_data,
                session_id=session_id
            )

            self.logger.info(f"Message processed: progress={updated_form_data.session_info.metadata.progress}%")  # Log info directly
            return updated_form_data

        except Exception as e:
            self.logger.error(f"Error processing message: {e}")
            self.logger.error(traceback.format_exc())

            # Return error response
            # Create session_info with empty form
            session_info = SessionInfo(
                user_form=self.form_class.model_construct(),
                metadata=FormMetadata(
                    next_message_ai="Could you try rephrasing your message?",
                    progress=0
                )
            )

            # Create FormData with session_info
            return FormData(
                session_info=session_info,
                system=System(completion_threshold=self.completion_threshold)
            )

    async def get_form_state(
        self,
        session_id: str
    ) -> FormData:
        """
        Retrieves the latest form state for a given session as a FormData object.

        Args:
            session_id: The identifier of the session.

        Returns:
            The FormData object representing the latest state.
            Returns an empty FormData object if the session or state is not found or fails to reconstruct.
        """
        if not session_id:
            self.logger.error("Session ID is required in get_form_state")  # Log error
            raise ValueError("Session ID is required")

        try:
            # Set current session
            self.session_manager.session_id = session_id

            # Get latest form data
            form_data_dict = await self.session_manager.get_latest_form_data(session_id)
            self.logger.info(f"Loaded form data dict from DB for get_form_state: {form_data_dict}")  # Log info directly
            if not form_data_dict:
                self.logger.warning(f"No form data found for session {session_id} in get_form_state, returning empty.")  # Log warning directly
                # Return empty form data if none exists, including system config
                # Create session_info with empty form
                session_info = SessionInfo(
                    user_form=self.form_class(),
                    metadata=FormMetadata()
                )

                # Return FormData with session_info
                return FormData(
                    session_info=session_info,
                    system=System(completion_threshold=self.completion_threshold)
                )

            # Reconstruct form data from dict
            try:
                form_instance = self.form_class.model_construct(
                    **form_data_dict.get("user_form", {})
                )
                metadata_dict = form_data_dict.get("metadata", {})
                system_dict = form_data_dict.get("system", {})
                analytics_dict = form_data_dict.get("analytics")

                # Reconstruct analytics if present
                analytics_obj = None
                if analytics_dict:
                    try:
                        analytics_obj = AnalyticsResult.model_validate(analytics_dict)
                    except Exception as analytics_exc:
                        self.logger.error(f"Error reconstructing analytics in get_form_state: {analytics_exc}")
                        # Keep analytics_obj as None if reconstruction fails

                # Create session_info
                session_info = SessionInfo(
                    user_form=form_instance,
                    metadata=FormMetadata.model_validate(metadata_dict)
                )

                # Create form_data with session_info
                form_data = FormData(
                    session_info=session_info,
                    system=System.model_validate(system_dict),
                    analytics=analytics_obj
                )
                return form_data
            except Exception as e:
                self.logger.error(f"Error reconstructing form data in get_form_state: {e}")
                # Fallback to empty form data on reconstruction error, including system config
                # Create session_info with empty form
                session_info = SessionInfo(
                    user_form=self.form_class(),
                    metadata=FormMetadata()
                )

                # Return FormData with session_info
                return FormData(
                    session_info=session_info,
                    system=System(completion_threshold=self.completion_threshold)
                )

        except Exception as e:
            self.logger.error(f"Error getting form state: {e}")
            self.logger.error(traceback.format_exc())
            # Fallback to empty form data on general error, including system config
            # Create session_info with empty form
            session_info = SessionInfo(
                user_form=self.form_class(),
                metadata=FormMetadata()
            )

            # Return FormData with session_info
            return FormData(
                session_info=session_info,
                system=System(completion_threshold=self.completion_threshold)
            )
