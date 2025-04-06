# Pydantic2 Agents - Form Processing with LLM

Framework for extracting structured data from dialogues using LLM models via OpenRouter.

## Capabilities

- Extraction of data from user messages and form field population
- Calculation of completion progress and detection of completion moment
- Analytics generation for completed forms
- Conversation history tracking
- Form state and message persistence in database
- Error handling and recovery after failures

## Architecture

### Core

- `FormProcessor` - main entry point for applications
- `FormAgent` - interaction with LLM and form data processing
- `SessionManager` - session management and state persistence

### Data Models

- `BaseFormModel` - base class for all form models
- `FormData` - container for form data and metadata
- `FormMetadata` - tracking progress, messages, language, etc.
- `AnalyticsResult` - analysis results for the completed form

### LLM Providers

- `OpenRouterProvider` - provider for OpenRouter LLM API
- `LLMResponse` - wrapper for LLM responses with simplified access

### Utilities

- `logging_config` - logging configuration
- `text_sanitizer` - cleaning text from potentially dangerous code
- `model_factory` - creation of model instances
- `schema_utils` - working with JSON schemas

## Usage Example

```python
from pydantic import Field
from pydantic2.agents import FormProcessor, BaseFormModel

# Define form model
class StartupForm(BaseFormModel):
    name: str = Field(default="", description="Startup name")
    description: str = Field(default="", description="Product/service description")
    industry: str = Field(default="", description="Industry/sector")
    funding: float = Field(default=0.0, description="Required investment in USD")
    team_size: int = Field(default=0, description="Team size")

# Initialize processor
processor = FormProcessor(
    form_class=StartupForm,
    api_key="your-api-key",
    role_prompt="Speak with the user in English",
    model_name="openai/gpt-4o-mini",
    completion_threshold=80
)

# Start session
session_id = await processor.start_session("user-id")

# Process messages
form_data = await processor.process_message("Hi, I have a startup called TechWave", session_id)
print(form_data.metadata.next_message_ai)
print(f"Progress: {form_data.metadata.progress}%")

# Get analytics after completion
if form_data.analytics:
    print(f"Data analysis: {form_data.analytics.data_summary}")
```

## Advantages

- Clean architecture with separation of concerns
- Direct LLM calls without complex agent frameworks
- Robust error handling and validation
- Asynchronous API for all major operations
- State persistence in SQLite database
