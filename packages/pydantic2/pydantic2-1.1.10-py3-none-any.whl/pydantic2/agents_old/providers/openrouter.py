"""OpenRouter provider for LLM services."""

import logging
import json
from typing import Dict, Any, Optional, List, Union
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("providers.openrouter")


class LLMResponse:
    """Wrapper for LLM response that simplifies access to content."""

    def __init__(self, response_data: Union[Dict[str, Any], ChatCompletion, str]):
        """Initialize with raw response data."""
        self.raw_response = response_data
        self._content = None
        self._extract_content()

    def _extract_content(self):
        """Extract content from various response formats."""
        try:
            # Direct string content
            if isinstance(self.raw_response, str):
                self._content = self.raw_response
            # Handle ChatCompletion object from openai
            elif isinstance(self.raw_response, ChatCompletion):
                if hasattr(self.raw_response, 'choices') and len(self.raw_response.choices) > 0:
                    if hasattr(self.raw_response.choices[0], 'message'):
                        self._content = self.raw_response.choices[0].message.content
            # Handle dict from OpenRouter
            elif isinstance(self.raw_response, dict) and 'choices' in self.raw_response:
                if isinstance(self.raw_response['choices'], list) and len(self.raw_response['choices']) > 0:
                    choice = self.raw_response['choices'][0]
                    if isinstance(choice, dict) and 'message' in choice:
                        self._content = choice['message'].get('content', '')
            # Fallback for unknown format
            else:
                logger.warning(f"Unknown response format: {type(self.raw_response)}")
                self._content = str(self.raw_response)
        except Exception as e:
            logger.error(f"Error extracting content from response: {e}")
            self._content = ""

    @property
    def content(self) -> str:
        """Get the response content."""
        return self._content or ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        if isinstance(self.raw_response, dict):
            return self.raw_response
        elif isinstance(self.raw_response, ChatCompletion):
            # Convert ChatCompletion to dict more safely
            try:
                return {
                    "id": getattr(self.raw_response, "id", "unknown"),
                    "object": getattr(self.raw_response, "object", "chat.completion"),
                    "created": getattr(self.raw_response, "created", 0),
                    "model": getattr(self.raw_response, "model", "unknown"),
                    "content": self.content
                }
            except Exception as e:
                logger.error(f"Error converting ChatCompletion to dict: {e}")
                return {"content": self.content}
        else:
            return {"content": self.content}


class OpenRouterProvider:
    """
    Provider for OpenRouter API for accessing models.

    This implementation works without requiring pydantic-ai
    and handles API responses properly.
    """

    def __init__(
        self,
        api_key: str,
        model_name: str = "openai/gpt-4o-mini",
        base_url: str = "https://openrouter.ai/api/v1",
        timeout: int = 60,
        max_retries: int = 2
    ):
        """
        Initialize OpenRouter provider.

        Args:
            api_key: API key for OpenRouter
            model_name: Model name to use
            base_url: Base URL for API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
        """
        if not api_key:
            raise ValueError("API key is required")

        self.api_key = api_key
        self.model_name = model_name

        # Create OpenAI client
        try:
            self.client = AsyncOpenAI(
                api_key=api_key,
                base_url=base_url,
                timeout=timeout,
                max_retries=max_retries
            )
            logger.debug(f"Created OpenAI client with model {model_name}")
        except Exception as e:
            logger.error(f"Error creating OpenAI client: {e}")
            raise ValueError(f"Failed to initialize OpenAI client: {str(e)}")

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> LLMResponse:
        """
        Generate chat completion directly.

        Args:
            messages: Chat messages
            temperature: Model temperature
            max_tokens: Maximum tokens to generate

        Returns:
            LLMResponse containing the completion
        """
        try:
            # Convert messages to proper format
            formatted_messages = []
            for msg in messages:
                if isinstance(msg, dict) and 'role' in msg and 'content' in msg:
                    formatted_messages.append({
                        "role": msg["role"],
                        "content": msg["content"]
                    })

            # Call the API
            kwargs = {
                "model": self.model_name,
                "messages": formatted_messages,
                "temperature": temperature
            }

            if max_tokens is not None:
                kwargs["max_tokens"] = max_tokens

            response = await self.client.chat.completions.create(**kwargs)

            return LLMResponse(response)

        except Exception as e:
            logger.error(f"Error in chat completion: {e}")
            return LLMResponse(f"Error: {str(e)}")

    async def json_completion(
        self,
        prompt: str,
        system_message: str = "You are a helpful assistant that responds with JSON.",
        temperature: float = 0.0
    ) -> Dict[str, Any]:
        """
        Generate completion and return as JSON.

        Args:
            prompt: User prompt
            system_message: System message
            temperature: Model temperature

        Returns:
            Dict containing parsed JSON response
        """
        try:
            # Set up messages
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]

            # Request JSON format if supported
            try:
                # First try with response_format
                kwargs = {
                    "model": self.model_name,
                    "messages": messages,
                    "temperature": temperature,
                    "response_format": {"type": "json_object"}
                }
                response = await self.client.chat.completions.create(**kwargs)
                response_obj = LLMResponse(response)
            except Exception as e:
                # Fallback to regular completion
                logger.warning(f"JSON response_format not supported: {e}, using regular completion")
                response_obj = await self.chat_completion(messages, temperature)

            # Parse JSON response
            try:
                return json.loads(response_obj.content)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {e}")
                # If we can't parse JSON, wrap the content in a basic JSON structure
                return {"error": "Failed to parse JSON", "content": response_obj.content}

        except Exception as e:
            logger.error(f"Error in json_completion: {e}")
            return {"error": str(e)}
