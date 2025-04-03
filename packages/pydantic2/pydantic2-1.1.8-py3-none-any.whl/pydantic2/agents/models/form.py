"""Form data models."""

import logging
from typing import Dict, Any, List, Type, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict, create_model, ValidationInfo

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("models.form")


class FormMetadata(BaseModel):
    """Metadata for forms including processing state."""
    next_message_ai: str = Field(default="", description="Next question to ask")
    progress: int = Field(default=0, description="Form completion progress (0-100)")
    history: List[str] = Field(default_factory=list, description="Message history")
    conversation_summary: List[str] = Field(default_factory=list, description="Summary of conversation")
    user_language: str = Field(default="en", description="Detected user language")
    completion_achieved: bool = Field(default=False, description="Whether form has been completed")
    analytics: Optional[BaseModel] = Field(default=None, description="Analytics of the form")
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        coerce_numbers_to_str=False
    )

    @classmethod
    def model_validate(cls, obj: Any, **kwargs) -> "FormMetadata":
        """Override model_validate to handle float progress values."""
        if isinstance(obj, dict) and "progress" in obj and isinstance(obj["progress"], float):
            obj = obj.copy()
            obj["progress"] = int(obj["progress"])
        return super().model_validate(obj, **kwargs)

    @field_validator("progress")
    @classmethod
    def validate_progress(cls, v) -> int:
        """Ensure progress is between 0 and 100 and convert to integer."""
        # Handle float values by converting to int
        if isinstance(v, float):
            v = int(v)
        return max(0, min(v, 100))

    @field_validator("completion_achieved")
    @classmethod
    def set_completion_from_progress(cls, v: bool, info: ValidationInfo) -> bool:
        """Set completion based on progress."""
        if "progress" in info.data and info.data["progress"] >= 100:
            return True
        return v


class BaseFormModel(BaseModel):
    """Base class for all form models."""
    model_config = ConfigDict(validate_assignment=True)


class FormData(BaseModel):
    """
    Container for form data and metadata.

    This class holds both the actual form model instance and associated metadata
    about form completion status, conversation history, etc.
    """
    form: BaseModel
    metadata: FormMetadata = Field(default_factory=FormMetadata)

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def create_empty(cls, form_class: Type[BaseModel]) -> "FormData":
        """Create an empty form data instance."""
        try:
            # Create an empty form instance safely with model_construct
            form_instance = form_class.model_construct()

            # Create initial metadata
            metadata = FormMetadata(
                next_message_ai="Let's start. What would you like to share first?"
            )

            return cls(form=form_instance, metadata=metadata)
        except Exception as e:
            logger.error(f"Failed to create empty form: {e}")
            raise ValueError(f"Failed to create empty form: {str(e)}")

    def safe_dict(self) -> Dict[str, Any]:
        """Convert to dictionary safely for serialization."""
        return {
            "form": self.form.model_dump() if hasattr(self.form, "model_dump") else {},
            "metadata": self.metadata.model_dump()
        }

    def update_form(self, new_form_data: Dict[str, Any]) -> None:
        """Update form data safely."""
        if not new_form_data:
            logger.warning("Empty form data provided for update")
            return

        try:
            # Get the current form as a dict
            current_data = self.form.model_dump() if hasattr(self.form, "model_dump") else {}

            # Update with new data
            current_data.update(new_form_data)

            # Create new form instance using model_construct to bypass validation
            form_class = self.form.__class__
            new_form = form_class.model_construct(**current_data)

            # Set the new form
            self.form = new_form

        except Exception as e:
            logger.error(f"Error updating form data: {e}")
            # Form remains unchanged

    def is_complete(self) -> bool:
        """Check if the form is complete."""
        return self.metadata.progress >= 100 or self.metadata.completion_achieved


def create_form_model(name: str, fields: Dict[str, Any]) -> Type[BaseFormModel]:
    """
    Create a form model dynamically.

    Args:
        name: Model name
        fields: Field definitions

    Returns:
        New form model class
    """
    return create_model(
        name,
        __base__=BaseFormModel,
        **fields
    )
