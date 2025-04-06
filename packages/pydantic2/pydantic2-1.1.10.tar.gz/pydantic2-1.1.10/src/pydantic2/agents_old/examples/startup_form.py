"""Example usage of the form processing framework with a startup form."""

import asyncio
import logging
import os
import json
from typing import List

from pydantic import Field
from pydantic2.agents import FormProcessor, BaseFormModel


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("examples.startup_form")


class StartupForm(BaseFormModel):
    """Form for collecting startup information."""
    name: str = Field(default="", description="Startup name")
    industry: str = Field(default="", description="Industry or sector")
    description: str = Field(default="", description="Brief description of the product/service")
    problem_statement: str = Field(default="", description="Problem the startup is solving")
    target_market: str = Field(default="", description="Target customer segments")
    business_model: str = Field(default="", description="How the startup makes money")
    competitors: List[str] = Field(default_factory=list, description="Main competitors")
    team_size: int = Field(default=0, description="Number of team members")
    funding_needed: float = Field(default=0.0, description="Funding amount needed in USD")
    funding_stage: str = Field(default="", description="Current funding stage (e.g., seed, Series A)")
    traction: str = Field(default="", description="Current traction metrics")
    location: str = Field(default="", description="Primary location/HQ")
    founding_year: int = Field(default=0, description="Year the startup was founded")


async def process_startup_form():
    """Example function for processing a startup form."""
    # Get API key from environment
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        logger.error("OPENROUTER_API_KEY environment variable not set")
        return

    # Initialize processor
    processor = FormProcessor(
        form_class=StartupForm,
        api_key=api_key,
        model_name="openai/gpt-4o-mini",  # Use a smaller model for testing
        verbose=True
    )

    try:
        # Start a new session
        session_id = await processor.start_session("example_user")
        logger.info(f"Started session: {session_id}")

        # Sample conversations
        # Английская версия примера (закомментирована)
        messages_en = [
            "Hi, I want to tell you about my startup called TechWave.",
            "We're building an AI-powered analytics platform for e-commerce businesses.",
            "We're targeting small to medium-sized online retailers who struggle with data analysis.",
            "We have 5 team members, all with background in ML and e-commerce.",
            "We're based in San Francisco and looking for $500,000 in seed funding.",
            "Our main competitors are Shopify Analytics, but our solution is more affordable and easier to use.",
            "We charge a monthly subscription fee based on store size, starting at $99/month.",
            "We already have 10 paying customers and have been growing 20% month over month.",
            "We started in 2022 and have been bootstrapped so far."
        ]

        # Русская версия примера
        messages_ru = [
            "Привет, я хочу рассказать вам о своем стартапе под названием TechWave.",
            "Мы строим платформу аналитики на основе ИИ для интернет-магазинов.",
            "Целевая аудитория - малые и средние интернет-магазины, которые испытывают трудности с анализом данных.",
            "У нас 5 членов команды, все из них имеют образование в области машинного обучения и электронной коммерции.",
            "Мы находимся в Сан-Франциско и ищем $500,000 в качестве стартового капитала.",
        ]

        # Process messages
        for msg in messages_en:
            logger.info(f"Processing message: {msg}")
            response = await processor.process_message(msg, session_id)

            # Создаем словарь для логирования с данными формы
            log_data = {
                "form": response.form.model_dump() if hasattr(response.form, "model_dump") else {},
                "metadata": response.metadata.model_dump() if hasattr(response.metadata, "model_dump") else {}
            }

            # Логируем данные в JSON формате для лучшей читаемости
            logger.info(json.dumps(log_data, indent=2, ensure_ascii=False))
            logger.info("-" * 50)

            # Wait a moment before next message to avoid overwhelming output
            await asyncio.sleep(0.5)

        # Get final form state
        form_state = await processor.get_form_state(session_id)
        logger.info("Final form data:")
        logger.info(form_state)

        # Final response
        logger.info("Response:")
        logger.info(response.model_dump_json(indent=2))

    except Exception as e:
        logger.error(f"Error in process_startup_form: {e}")


if __name__ == "__main__":
    asyncio.run(process_startup_form())
