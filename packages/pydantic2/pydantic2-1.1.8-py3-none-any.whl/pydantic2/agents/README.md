# Agents7 - Form Processing Framework with Improved Model Structure

This version of the form processing framework introduces a cleaner architecture with separate models for form data and analytics.

## Key Improvements

### 1. Better Model Structure

- **Form Model**: Focused on representing and manipulating form data
  - `BaseFormModel`: Base class for all form models
  - `FormData`: Container with form and metadata
  - `FormMetadata`: Stores processing state and history

- **Analytics Model**: Dedicated to analytics results
  - `AnalyticsResult`: Contains insights, recommendations, scoring

### 2. Simplified Architecture

- Direct LLM calls rather than complex agent frameworks
- Better error handling and validation
- Cleaner, more modular code structure
- No dependency on external agent frameworks

### 3. Improved Error Handling

- Fallback strategies at every level
- Comprehensive error logging
- Graceful recovery from failures

### 4. Better Persistence

- Improved session handling
- Database storage for form data and messages
- Message history tracking

## Usage

```python
from pydantic import BaseModel, Field
from pydantic2.agents7 import FormProcessor, BaseFormModel

# Define your form model
class StartupForm(BaseFormModel):
    name: str = Field(default="", description="Startup name")
    description: str = Field(default="", description="Startup description")
    industry: str = Field(default="", description="Industry sector")
    funding: float = Field(default=0.0, description="Funding needed in USD")
    team_size: int = Field(default=0, description="Number of team members")

# Initialize processor
processor = FormProcessor(
    form_class=StartupForm,
    api_key="your-api-key"
)

# Start session
session_id = await processor.start_session("user-id")

# Process messages
response = await processor.process_message("Hello, I have a startup called TechWave", session_id)
print(response["message"])
print(f"Progress: {response['progress']}%")
```

## Key Components

### Core Components

- `FormProcessor`: Main entry point for applications
- `FormAgent`: Handles the LLM interaction and form processing
- `SessionManager`: Manages persistence of sessions and messages

### Models

- `BaseFormModel`: Base for all form models
- `FormData`: Container for form data and metadata
- `FormMetadata`: Tracks progress, messages, language, etc.
- `AnalyticsResult`: Contains analytics results and insights

### Providers

- `OpenRouterProvider`: Provider for OpenRouter LLM API
- `LLMResponse`: Wrapper for LLM responses with simplified access

## Key Features

- Form data extraction from user messages
- Progress calculation
- Conversation history tracking
- Form completion detection
- Analytics generation for completed forms
- Session persistence
- Error recovery
