"""Form processor for handling user interaction."""

import logging
import traceback
from typing import Dict, Any, Optional, Type

from pydantic import BaseModel

from ..models.form import FormData, BaseFormModel, FormMetadata
from .agent import FormAgent
from .session import SessionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("core.processor")


# Disable DEBUG logs for external libraries
logging.getLogger("httpcore.http11").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


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
        model_name: str = "openai/gpt-4o-mini",
        temperature: float = 0.1,
        db_path: Optional[str] = None,
        client_id: str = "default",
        verbose: bool = False
    ):
        """
        Initialize form processor.

        Args:
            form_class: Form class
            api_key: API key for LLM provider
            model_name: Model name to use
            temperature: Temperature for LLM generation
            db_path: Path to database for session persistence
            client_id: Client identifier
            verbose: Enable verbose logging
        """
        self.form_class = form_class
        self.client_id = client_id
        self.verbose = verbose

        # Validate inputs
        if not api_key:
            raise ValueError("API key is required")

        if not issubclass(form_class, BaseModel):
            raise ValueError("Form class must be a subclass of BaseModel")

        try:
            # Initialize form agent
            self.agent = FormAgent(
                api_key=api_key,
                model_name=model_name,
                temperature=temperature,
                verbose=verbose
            )
            logger.info(f"Form agent initialized with model {model_name}")
        except Exception as e:
            logger.error(f"Failed to initialize form agent: {e}")
            raise ValueError(f"Failed to initialize form agent: {str(e)}")

        try:
            # Initialize session manager
            self.session_manager = SessionManager(
                db_path=db_path,
                verbose=verbose
            )
            logger.info("Session manager initialized")
        except Exception as e:
            logger.error(f"Failed to initialize session manager: {e}")
            raise ValueError(f"Failed to initialize session manager: {str(e)}")

    async def start_session(self, user_id: str) -> str:
        """
        Start a new form processing session.

        Args:
            user_id: User identifier

        Returns:
            Session identifier
        """
        try:
            # Create a new session
            session_id = await self.session_manager.create_session(
                user_id=user_id,
                client_id=self.client_id,
                form_class=self.form_class.__name__
            )

            # Create empty form data
            form_data = FormData.create_empty(self.form_class)

            # Save initial form data
            await self.session_manager.save_form_data(form_data, session_id)

            # Save welcome message
            await self.session_manager.save_message(
                role="assistant",
                content=form_data.metadata.next_message_ai,
                session_id=session_id
            )

            logger.info(f"Started new session: {session_id}")
            return session_id

        except Exception as e:
            logger.error(f"Error starting session: {e}")
            logger.error(traceback.format_exc())
            raise ValueError(f"Failed to start session: {str(e)}")

    async def process_message(
        self,
        message: str,
        session_id: str
    ) -> FormData:
        """
        Process a user message and update form state.

        Args:
            message: User message
            session_id: Session identifier

        Returns:
            Updated form data
        """
        if not session_id:
            raise ValueError("Session ID is required")

        try:
            # Set current session
            self.session_manager.session_id = session_id

            # Get session info to verify session exists
            session_info = await self.session_manager.get_session_info(session_id)
            if not session_info:
                raise ValueError(f"Session not found: {session_id}")

            # Get message history
            message_history = await self.session_manager.get_messages(session_id)

            # Save user message
            await self.session_manager.save_message(
                role="user",
                content=message,
                session_id=session_id
            )

            # Get latest form data
            form_data_dict = await self.session_manager.get_latest_form_data(session_id)
            if not form_data_dict:
                logger.warning(f"No form data found for session {session_id}, creating empty")
                form_data = FormData.create_empty(self.form_class)
            else:
                try:
                    # Reconstruct form data from dict
                    form_instance = self.form_class.model_construct(
                        **form_data_dict.get("form", {})
                    )

                    # Use model_validate for metadata to properly handle type conversion
                    metadata_dict = form_data_dict.get("metadata", {})

                    # Create FormData with metadata model validation
                    form_data = FormData(
                        form=form_instance,
                        metadata=FormMetadata.model_validate(metadata_dict)
                    )
                except Exception as e:
                    logger.error(f"Error reconstructing form data: {e}")
                    # Fallback to empty form data
                    form_data = FormData.create_empty(self.form_class)

            # Process message with agent
            updated_form_data = await self.agent.process_message(
                message=message,
                form_data=form_data,
                form_class=self.form_class,
                message_history=message_history
            )

            # Save assistant message
            await self.session_manager.save_message(
                role="assistant",
                content=updated_form_data.metadata.next_message_ai,
                session_id=session_id
            )

            # Save updated form data
            await self.session_manager.save_form_data(
                form_data=updated_form_data,
                session_id=session_id
            )

            logger.info(f"Message processed: progress={updated_form_data.metadata.progress}%")
            return updated_form_data

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            logger.error(traceback.format_exc())

            # Return error response
            return FormData(
                form=self.form_class.model_construct(),
                metadata=FormMetadata(
                    next_message_ai="Could you try rephrasing your message?",
                    progress=0
                )
            )

    async def get_form_state(
        self,
        session_id: str
    ) -> Dict[str, Any]:
        """
        Get current form state.

        Args:
            session_id: Session identifier

        Returns:
            Form state data
        """
        if not session_id:
            raise ValueError("Session ID is required")

        try:
            # Set current session
            self.session_manager.session_id = session_id

            # Get latest form data
            form_data_dict = await self.session_manager.get_latest_form_data(session_id)
            if not form_data_dict:
                raise ValueError(f"No form data found for session {session_id}")

            # Return form state
            return form_data_dict

        except Exception as e:
            logger.error(f"Error getting form state: {e}")
            logger.error(traceback.format_exc())
            return {"error": str(e)}
