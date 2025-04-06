"""Interactive example of the form processing framework with user input via console."""

import asyncio
import os
from typing import List
from datetime import datetime
import questionary
from pydantic import BaseModel, Field
from pydantic2.agents import FormProcessor, BaseFormModel, FormData
from pydantic2.agents.utils.logging_config import SimpleLogger, LogConsole
import nest_asyncio

nest_asyncio.apply()

# Create a logger using our SimpleLogger class
logger = SimpleLogger("examples.interactive_form")
logger.set_agents_logs_visible(True)

console = LogConsole(
    name="examples.interactive_form"
)


# Создаем вложенные модели 3-го уровня
class ContactInfo(BaseModel):
    """Контактная информация."""
    email: str = Field(default="", description="Email контакт")
    phone: str = Field(default="", description="Телефонный номер")
    website: str = Field(default="", description="Веб-сайт")


class MarketInfo(BaseModel):
    """Информация о рынке."""
    size: str = Field(default="", description="Размер рынка")
    growth_rate: float = Field(default=0.0, description="Темпы роста рынка в %")
    competitors: List[str] = Field(default_factory=list, description="Список конкурентов")


class StartupForm(BaseFormModel):
    """Form for collecting startup information."""
    name: str = Field(default="", description="Название стартапа")
    description: str = Field(default="", description="Описание продукта/сервиса")
    industry: str = Field(default="", description="Отрасль/сектор")
    problem_statement: str = Field(default="", description="Проблема, которую решает стартап")
    market: MarketInfo = Field(default_factory=MarketInfo, description="Информация о рынке")
    contact: ContactInfo = Field(default_factory=ContactInfo, description="Контактная информация")


def get_user_input() -> str:
    """Get input from user with questionary."""
    response = questionary.text("\n💬 Ваш ответ (введите 'exit' для выхода):").ask()
    if response is None:  # Пользователь нажал Ctrl+C
        return "exit"
    return response


def create_progress_bar(percentage: int, width: int = 20) -> str:
    """Create a text-based progress bar."""
    filled_width = int(width * percentage / 100)
    bar = "█" * filled_width + "░" * (width - filled_width)
    return bar


class InteractiveFormSession:
    """Class to handle the interactive form session."""

    def __init__(self):
        self.processor = None
        self.processor_session_id = None
        self.logger = logger.bind(session_id=f"session_{datetime.now().strftime('%Y%m%d%H%M%S')}")

    def setup(self):
        """Initialize the processor with user preferences."""
        # Get API key from environment
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            self.logger.error("OPENROUTER_API_KEY environment variable not set")
            print("\n❌ Переменная окружения OPENROUTER_API_KEY не установлена. Пожалуйста, установите её и попробуйте снова.")
            return False

        # Установка русского языка по умолчанию
        role_prompt = """
        Говори с пользователем на его языке и будь лаконичным.
        Задавай конкретные вопросы о стартапе.
        Будь саркастичным и общайся в стиле Пелевина.
        """

        # Initialize processor
        try:
            self.logger.info("Initializing FormProcessor...")
            self.processor = FormProcessor(
                form_class=StartupForm,
                api_key=api_key,
                model_name="openai/gpt-4o-mini",
                completion_threshold=100,  # Set lower threshold to trigger analytics
                role_prompt=role_prompt,
                verbose=True  # Enable detailed logging
            )
            self.logger.info("Form processor initialized successfully")
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize processor: {e}")
            print(f"\n❌ Ошибка инициализации процессора: {e}")
            return False

    async def initialize_session(self):
        """Initialize session asynchronously."""
        if not self.processor:
            self.logger.error("Processor not initialized")
            return None

        self.processor_session_id = await self.processor.start_session("interactive_user")
        self.logger = self.logger.bind(processor_session_id=self.processor_session_id)
        self.logger.success("Session started successfully")

        # Get initial response
        form_data = await self.processor.get_form_state(self.processor_session_id)
        initial_message = form_data.session_info.metadata.next_message_ai or "Привет! Я помогу вам заполнить форму для стартапа. Давайте начнем!"

        # Показываем начальное состояние формы перед приветствием
        console.print_json(message="Initial form data", data=form_data.session_info.user_form.model_dump())

        # Только потом приветствие AI
        print(f"\n🤖 {initial_message}")

        return form_data

    async def process_user_message(self, user_message):
        """Process a single user message."""
        if not self.processor or not self.processor_session_id:
            self.logger.error("Processor or session not initialized")
            return None

        self.logger.info(f"Processing user message: {user_message}")
        response = await self.processor.process_message(user_message, str(self.processor_session_id))

        # Show progress
        progress = response.session_info.metadata.progress
        progress_bar = create_progress_bar(progress)
        print(f"\n📊 Заполнение формы: {progress_bar} {progress}%")

        # Всегда показывать текущие данные формы ПЕРЕД ответом AI
        console.print_json(message="Session info", data=response.session_info.model_dump())

        # Show AI response ПОСЛЕ вывода данных формы
        print(f"\n🤖 {response.session_info.metadata.next_message_ai}")

        return response

    async def handle_form_completion(self, response: FormData):
        """Handle form completion if achieved."""
        if not response:
            return False

        if response.system.completion_achieved:
            self.logger.success("Form reached completion threshold!")

            if response.analytics:
                print("\n📈 Анализ формы завершен!")
                return True

        return False


async def async_main():
    """Asynchronous main function."""
    print("🚀 Запуск интерактивного примера заполнения формы\n")
    print("Этот пример позволяет интерактивно заполнить форму для стартапа через диалог.")
    print("Введите 'exit' в любой момент, чтобы выйти из диалога.\n")

    # Initialize session
    session = InteractiveFormSession()
    if not session.setup():
        return

    try:
        # Initialize session asynchronously
        await session.initialize_session()

        # Main loop (handled synchronously to avoid questionary asyncio issues)
        user_message = get_user_input()

        while user_message.lower() not in ['exit', 'quit', 'q']:
            # Process message asynchronously
            response = await session.process_user_message(user_message)

            if not response:
                print("\n❌ Не удалось обработать сообщение")
                break

            # Check if form is complete
            form_completed = await session.handle_form_completion(response)

            if form_completed and response.analytics:
                # Using a direct approach without questionary for analytics display
                print("\n📈 Анализ формы завершен!")
                show_analytics = input("Показать аналитику? (y/n): ").lower().startswith('y')
                if show_analytics:
                    console.print_json(message="Form analytics", data=response.analytics.model_dump())

                # And for continuation question
                continue_conversation = input("Хотите продолжить разговор? (y/n): ").lower().startswith('y')
                if not continue_conversation:
                    print("\n👋 Спасибо за заполнение формы!")
                    break

            # Get next user message
            user_message = get_user_input()

        print("\n👋 Завершение диалога. Спасибо за ваше время!")

    except Exception as e:
        logger.exception(f"Error during conversation: {e}")
        print(f"\n❌ Произошла ошибка: {e}")


def main():
    """Main entry point for the interactive form example."""
    try:
        asyncio.run(async_main())
        print("\n✅ Пример завершен")
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана. Завершение работы.")
    except Exception as e:
        logger.exception(f"Unhandled error: {e}")
        print(f"\n❌ Произошла необработанная ошибка: {e}")


if __name__ == "__main__":
    main()
