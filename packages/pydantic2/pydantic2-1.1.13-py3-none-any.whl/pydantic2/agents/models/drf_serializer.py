from drf_pydantic import BaseModel
from pydantic import Field
from typing import List

from .form import MessageHistory


class Pyndatic2UserForm(BaseModel):
    """Base class for defining the structure of a specific form."""
    pass


class Pyndatic2UserInfo(BaseModel):
    """Base class for defining the structure of a specific form."""
    name: str = Field(default=None)


class Pyndatic2FormMetadata(BaseModel):
    """Base class for defining the structure of a specific form."""
    next_message_ai: str = Field(default=None)
    progress: int = Field(default=0)
    user_info: Pyndatic2UserInfo = Field(default=None)
    user_language: str = Field(default=None)


class Pyndatic2SessionInfo(BaseModel):
    """Base class for defining the structure of a specific form."""
    user_form: Pyndatic2UserForm = Field(default=None)
    metadata: Pyndatic2FormMetadata = Field(default=None)


class Pyndatic2System(BaseModel):
    """Base class for defining the structure of a specific form."""
    completion_threshold: int = Field(default=100)
    completion_achieved: bool = Field(default=False)
    session_id: str = Field(default=None)
    client_id: str = Field(default=None)
    role_prompt: str = Field(default=None)
    model_name: str = Field(default=None)
    temperature: float = Field(default=None)
    form_defaults: Pyndatic2UserForm = Field(default=None)


class Pyndatic2Analytics(BaseModel):
    """Base class for defining the structure of a specific form."""
    pass


class Pyndatic2AgentResponse(BaseModel):
    """Base class for defining the structure of a specific form."""
    session_info: Pyndatic2SessionInfo = Field(default=None)
    system: Pyndatic2System = Field(default=None)
    analytics: Pyndatic2Analytics = Field(default=None)
    history: List[MessageHistory] = Field(default=None)
