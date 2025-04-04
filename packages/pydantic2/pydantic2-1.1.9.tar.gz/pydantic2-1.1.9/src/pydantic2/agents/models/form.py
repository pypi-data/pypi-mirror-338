"""Form data models."""

from .analytics import AnalyticsResult
from typing import Dict, Any, List, Type, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict, create_model
from pydantic import field_serializer
from ..utils.logging_config import SimpleLogger


logger = SimpleLogger("models.form")


class BaseFormModel(BaseModel):
    """Base class for defining the structure of a specific form."""
    model_config = ConfigDict(validate_assignment=True)


class FormMetadata(BaseModel):
    """Metadata associated with the form processing state."""
    next_message_ai: str = Field(default="", description="Next question to ask the user")
    progress: int = Field(default=0, description="Form completion progress (0-100)")
    history: List[str] = Field(default_factory=list, description="Message history")
    user_language: str = Field(default="en", description="Detected user language")
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        coerce_numbers_to_str=False
    )

    @classmethod
    def model_validate(cls, obj: Any, **kwargs) -> "FormMetadata":
        """Override model_validate to handle potential float progress values from LLM."""
        if isinstance(obj, dict) and "progress" in obj and isinstance(obj["progress"], float):
            logger.warning(f"Received float progress '{obj['progress']}', converting to int.")
            obj = obj.copy()
            obj["progress"] = int(obj["progress"])
        return super().model_validate(obj, **kwargs)

    @field_validator("progress")
    @classmethod
    def validate_progress(cls, v) -> int:
        """Ensure progress is an integer between 0 and 100."""
        if isinstance(v, float):
            logger.warning(f"Progress validator received float '{v}', converting to int.")
            v = int(v)
        if not 0 <= v <= 100:
            logger.warning(f"Progress {v} out of range (0-100), clamping.")
            v = max(0, min(v, 100))
        return v


class System(BaseModel):
    """System configuration for the form processing, including session and model parameters."""
    # Core settings
    completion_threshold: int = 100
    completion_achieved: bool = False

    # Added context fields
    session_id: Optional[str] = Field(default=None, description="Unique session identifier")
    client_id: Optional[str] = Field(default=None, description="Client application identifier")
    role_prompt: Optional[str] = Field(default=None, description="LLM role definition prompt")
    model_name: Optional[str] = Field(default=None, description="LLM model name used for the session")
    temperature: Optional[float] = Field(default=None, description="LLM temperature setting")
    form_defaults: Optional[Dict[str, Any]] = Field(default=None, description="Default values of the form model fields")

    model_config = ConfigDict(validate_assignment=True)


class FormData(BaseModel):
    """
    Container for form data and metadata.

    This class holds both the actual form model instance (inheriting from BaseFormModel)
    and associated metadata about the form completion status, conversation history,
    system configuration, and analytics results.
    """
    user_form: BaseModel
    metadata: FormMetadata = Field(default_factory=FormMetadata)
    system: System = Field(default_factory=System)
    analytics: Optional[AnalyticsResult] = Field(default=None, description="Analytics results of the form")

    @field_serializer('user_form')
    def serialize_user_form(self, v: BaseModel):
        return v.model_dump()

    def update_progress(self, new_progress: int):
        """Updates the progress and recalculates the completion status based on the threshold."""
        old_progress = self.metadata.progress
        self.metadata.progress = max(0, min(new_progress, 100))
        old_completion_status = self.system.completion_achieved
        self.system.completion_achieved = self.metadata.progress >= self.system.completion_threshold
        if old_progress != self.metadata.progress:
            logger.info(f"Progress updated: {old_progress}% -> {self.metadata.progress}%")
        if old_completion_status != self.system.completion_achieved:
            logger.info(f"Completion status changed: {old_completion_status} -> {self.system.completion_achieved}")

    def update_form(self, data: dict):
        """Updates the fields of the nested form model with new data."""
        if not isinstance(self.user_form, BaseModel):
            logger.error("Form field is not a Pydantic model, cannot update.")
            return

        updated_fields = []
        for key, value in data.items():
            if hasattr(self.user_form, key):
                try:
                    current_value = getattr(self.user_form, key)
                    if current_value != value:
                        setattr(self.user_form, key, value)
                        updated_fields.append(key)
                        logger.info(f"Updated form field '{key}'")
                    # else: logger.debug(f"Skipping update for field '{key}', value unchanged.")
                except Exception as e:
                    logger.warning(f"Failed to set attribute '{key}' on form: {e}")
            else:
                logger.warning(f"Attribute '{key}' not found in form model {self.user_form.__class__.__name__}")
        if updated_fields:
            logger.info(f"Fields updated in form: {', '.join(updated_fields)}")

    @classmethod
    def create_empty(cls, form_class: Type[BaseFormModel]) -> "FormData":
        """Creates an empty FormData instance for a given form class."""
        logger.info(f"Creating empty FormData for {form_class.__name__}")
        return cls(user_form=form_class())

    def safe_dict(self) -> Dict[str, Any]:
        """Converts the FormData object to a dictionary suitable for serialization."""
        try:
            # Выведем дополнительное логирование
            logger.debug(f"safe_dict: Converting FormData to dict. Has user_form: {hasattr(self, 'user_form') and self.user_form is not None}")

            # Сначала проверяем, что user_form существует и не None
            if not hasattr(self, 'user_form') or self.user_form is None:
                logger.warning("safe_dict: user_form is missing or None!")
                user_form_dict = {}
            else:
                # Затем пробуем получить словарь из user_form
                try:
                    user_form_dict = self.user_form.model_dump()
                    logger.debug(f"safe_dict: user_form successfully dumped, fields: {self.user_form.model_fields_set}")
                except Exception as e:
                    logger.error(f"safe_dict: Error converting user_form to dict: {e}")
                    user_form_dict = {}

            # Подготавливаем словарь метаданных
            metadata_dict = self.metadata.model_dump() if hasattr(self, 'metadata') and self.metadata is not None else {}
            system_dict = self.system.model_dump() if hasattr(self, 'system') and self.system is not None else {}

            # Подготавливаем словарь аналитики, если есть
            analytics_dict = None
            if hasattr(self, 'analytics') and self.analytics is not None:
                try:
                    analytics_dict = self.analytics.model_dump()
                except Exception as e:
                    logger.error(f"safe_dict: Error converting analytics to dict: {e}")

            # Создаем итоговый словарь
            data = {
                "user_form": user_form_dict,
                "metadata": metadata_dict,
                "system": system_dict,
                "analytics": analytics_dict
            }

            # Выводим информацию о данных в словаре
            logger.debug(f"safe_dict: Final dict structure: user_form keys: {list(user_form_dict.keys() if user_form_dict else [])}")

            return data
        except Exception as e:
            logger.error(f"Error creating safe_dict for FormData: {e}")
            return {}


def create_form_model(name: str, fields: Dict[str, Any]) -> Type[BaseFormModel]:
    """Dynamically creates a Pydantic model inheriting from BaseFormModel."""
    logger.info(f"Dynamically creating form model '{name}'")
    return create_model(name, __base__=BaseFormModel, **fields)
