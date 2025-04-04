"""Session manager for form persistence."""

import uuid
import json
import logging
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import peewee
from peewee import DoesNotExist

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("core.session")


CURRENT_DIR = Path(__file__).parent  # core/src
MODULE_DIR = CURRENT_DIR.parent.parent  # pydantic2
DB_DIR = MODULE_DIR / "db"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "sessions.db"

# Database models
database = peewee.SqliteDatabase(None)


class BaseModel(peewee.Model):
    """Base model for database tables."""
    class Meta:
        """Model metadata."""
        database = database


class Session(BaseModel):
    """Session information."""
    session_id = peewee.CharField(primary_key=True, max_length=255)
    user_id = peewee.CharField(max_length=255)
    client_id = peewee.CharField(max_length=255)
    form_class = peewee.CharField(max_length=255)
    created_at = peewee.DateTimeField()


class Message(BaseModel):
    """Message in a session."""
    id = peewee.AutoField()
    session_id = peewee.ForeignKeyField(Session, column_name='session_id', backref='messages')
    role = peewee.CharField(max_length=255)
    content = peewee.TextField()
    created_at = peewee.DateTimeField()


class State(BaseModel):
    """Form state."""
    id = peewee.AutoField()
    session_id = peewee.ForeignKeyField(Session, column_name='session_id', backref='states')
    data = peewee.TextField()
    created_at = peewee.DateTimeField()


class SessionManager:
    """
    Manager for user sessions and form data persistence.

    This class handles saving and retrieving form data,
    messages, and other session information.
    """

    def __init__(
        self,
        db_path: Optional[str] = None,
        verbose: bool = False
    ):
        """
        Initialize session manager.

        Args:
            db_path: Path to database file
            verbose: Enable verbose logging
        """
        self.verbose = verbose
        self.session_id = None

        # Set up database
        db_file = db_path or DB_PATH

        # Initialize database
        database.init(db_file)
        database.connect()

        # Create tables if they don't exist
        database.create_tables([Session, Message, State])

        logger.info(f"Database setup complete. Database path: {db_file}")

    async def create_session(
        self,
        user_id: str,
        client_id: str,
        form_class: str
    ) -> str:
        """
        Create a new session.

        Args:
            user_id: User identifier
            client_id: Client identifier
            form_class: Form class name

        Returns:
            Session identifier
        """
        try:
            session_id = str(uuid.uuid4())

            # Create session in database
            with database.atomic():
                Session.create(
                    session_id=session_id,
                    user_id=user_id,
                    client_id=client_id,
                    form_class=form_class,
                    created_at=datetime.now()
                )

            # Set current session
            self.session_id = session_id

            logger.info(f"Created session: {session_id}")
            return session_id
        except Exception as e:
            logger.error(f"Error creating session: {e}")
            logger.error(traceback.format_exc())
            raise

    async def save_message(
        self,
        role: str,
        content: str,
        session_id: Optional[str] = None
    ) -> bool:
        """
        Save message to session.

        Args:
            role: Message role (user or assistant)
            content: Message content
            session_id: Session identifier (if None, use current session)

        Returns:
            Success status
        """
        sid = session_id or self.session_id
        if not sid:
            raise ValueError("No active session")

        try:
            # Save message to database
            with database.atomic():
                Message.create(
                    session_id=sid,
                    role=role,
                    content=content,
                    created_at=datetime.now()
                )

            return True
        except Exception as e:
            logger.error(f"Error saving message: {e}")
            logger.error(traceback.format_exc())
            return False

    async def get_messages(
        self,
        session_id: Optional[str] = None,
        limit: int = 20
    ) -> List[Dict[str, Any]]:
        """
        Get messages from session.

        Args:
            session_id: Session identifier (if None, use current session)
            limit: Maximum number of messages to return

        Returns:
            List of messages
        """
        sid = session_id or self.session_id
        if not sid:
            raise ValueError("No active session")

        try:
            # Get messages from database
            query = (Message
                     .select()
                     .where(Message.session_id == sid)
                     .order_by(Message.created_at.asc())
                     .limit(limit))

            # Convert to list of dictionaries
            messages = []
            for msg in query:
                messages.append({
                    "role": msg.role,
                    "content": msg.content,
                    "created_at": msg.created_at.isoformat()
                })

            return messages
        except Exception as e:
            logger.error(f"Error getting messages: {e}")
            logger.error(traceback.format_exc())
            return []

    async def save_form_data(
        self,
        form_data: Any,
        session_id: Optional[str] = None
    ) -> bool:
        """
        Save form data.

        Args:
            form_data: Form data to save
            session_id: Session identifier (if None, use current session)

        Returns:
            Success flag
        """
        sid = session_id or self.session_id
        if not sid:
            raise ValueError("No active session")

        try:
            # Convert form data to dictionary
            data_dict = form_data.safe_dict() if hasattr(form_data, "safe_dict") else form_data

            # Convert float progress to int if it exists
            if isinstance(data_dict, dict) and "metadata" in data_dict and "progress" in data_dict["metadata"]:
                if isinstance(data_dict["metadata"]["progress"], float):
                    data_dict["metadata"]["progress"] = int(data_dict["metadata"]["progress"])

            # Serialize form data
            data_json = json.dumps(data_dict, ensure_ascii=False)

            # Save state to database
            with database.atomic():
                State.create(
                    session_id=sid,
                    data=data_json,
                    created_at=datetime.now()
                )

            return True
        except Exception as e:
            logger.error(f"Error saving form data: {e}")
            logger.error(traceback.format_exc())
            return False

    async def get_latest_form_data(
        self,
        session_id: Optional[str] = None,
        form_class=None
    ) -> Optional[Dict[str, Any]]:
        """
        Get latest form data from session.

        Args:
            session_id: Session identifier (if None, use current session)
            form_class: Form class for creating empty form data

        Returns:
            Latest form data or None if not found
        """
        sid = session_id or self.session_id
        if not sid:
            raise ValueError("No active session")

        try:
            # Get latest state from database
            query = (State
                     .select()
                     .where(State.session_id == sid)
                     .order_by(State.created_at.desc())
                     .limit(1))

            # Return state data if found
            for state in query:
                return json.loads(state.data)

            # No state found
            return None

        except Exception as e:
            logger.error(f"Error getting latest form data: {e}")
            logger.error(traceback.format_exc())
            return None

    async def get_session_info(
        self,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get session information.

        Args:
            session_id: Session identifier (if None, use current session)

        Returns:
            Session information
        """
        sid = session_id or self.session_id
        if not sid:
            raise ValueError("No active session")

        try:
            # Get session from database
            session = Session.get(Session.session_id == sid)

            # Return session information
            return {
                "session_id": session.session_id,
                "user_id": session.user_id,
                "client_id": session.client_id,
                "form_class": session.form_class,
                "created_at": session.created_at.isoformat()
            }
        except DoesNotExist:
            logger.error(f"Session not found: {sid}")
            return {}
        except Exception as e:
            logger.error(f"Error getting session info: {e}")
            logger.error(traceback.format_exc())
            return {}
