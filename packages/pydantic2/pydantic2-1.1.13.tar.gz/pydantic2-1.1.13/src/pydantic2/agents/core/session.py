"""Session manager for form persistence."""

import uuid
import json
import traceback
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import peewee
from peewee import DoesNotExist
from ..utils.logging_config import SimpleLogger
from ..models.form import MessageHistory

CURRENT_DIR = Path(__file__).parent  # core/src
MODULE_DIR = CURRENT_DIR.parent.parent  # pydantic2
DB_DIR = MODULE_DIR / "db"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "sessions.db"

# Database models
database = peewee.SqliteDatabase(None)


class BaseModel(peewee.Model):
    """Base model for Peewee database tables."""
    class Meta:
        """Model configuration."""
        database = database


class Session(BaseModel):
    """Represents a form processing session in the database."""
    session_id = peewee.CharField(primary_key=True, max_length=255)
    user_id = peewee.CharField(max_length=255)
    client_id = peewee.CharField(max_length=255)
    form_class = peewee.CharField(max_length=255)
    created_at = peewee.DateTimeField()


class Message(BaseModel):
    """Represents a single message within a session."""
    id = peewee.AutoField()
    session_id = peewee.ForeignKeyField(Session, column_name='session_id', backref='messages')
    role = peewee.CharField(max_length=255)
    content = peewee.TextField()
    created_at = peewee.DateTimeField()


class State(BaseModel):
    """Represents a snapshot of the form data state at a point in time."""
    id = peewee.AutoField()
    session_id = peewee.ForeignKeyField(Session, column_name='session_id', backref='states')
    data = peewee.TextField()
    created_at = peewee.DateTimeField()


class SessionManager:
    """
    Manages user sessions and persistence of form data and messages
    using a SQLite database.
    """

    def __init__(
        self,
        db_path: Optional[str] = None
    ):
        """
        Initializes the SessionManager and sets up the database connection.

        Args:
            db_path: Optional path to the SQLite database file. Defaults to 'db/sessions.db'.
        """
        self.logger = SimpleLogger("core.session")
        self.session_id = None

        # Set up database
        db_file = db_path or DB_PATH

        # Initialize database
        database.init(db_file)
        database.connect()

        # Create tables if they don't exist
        database.create_tables([Session, Message, State])

        self.logger.info(f"Database setup complete. Database path: {db_file}")

    async def create_session(
        self,
        user_id: str,
        client_id: str,
        form_class: str
    ) -> str:
        """
        Creates a new session record in the database.

        Args:
            user_id: The identifier for the user creating the session.
            client_id: An identifier for the client application.
            form_class: The name of the Pydantic form model class being used.

        Returns:
            The newly generated session ID.
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

            self.logger.info(f"Created session: {session_id}")
            return session_id
        except Exception as e:
            self.logger.error(f"Error creating session: {e}")
            self.logger.error(traceback.format_exc())
            raise

    async def save_message(
        self,
        role: str,
        content: str,
        session_id: Optional[str] = None
    ) -> bool:
        """
        Saves a message associated with a session to the database.

        Args:
            role: The role of the message sender ('user' or 'assistant').
            content: The text content of the message.
            session_id: The ID of the session. Uses the manager's current session ID if None.

        Returns:
            True if saving was successful, False otherwise.
        """
        sid = session_id or self.session_id
        if not sid:
            self.logger.error("No active session ID provided for save_message")
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
            self.logger.info(f"Saved message for session {sid} (Role: {role})")
            return True
        except Exception as e:
            self.logger.error(f"Error saving message for session {sid}: {e}")
            self.logger.error(traceback.format_exc())
            return False

    async def get_messages(
        self,
        session_id: Optional[str] = None,
        limit: int = 20
    ) -> List[MessageHistory]:
        """
        Retrieves messages for a specific session from the database.

        Args:
            session_id: The ID of the session. Uses the manager's current session ID if None.
            limit: The maximum number of recent messages to retrieve.

        Returns:
            A list of messages, each represented as a dictionary.
        """
        sid = session_id or self.session_id
        if not sid:
            self.logger.error("No active session ID provided for get_messages")
            raise ValueError("No active session")

        try:
            # Get messages from database
            query = (Message
                     .select()
                     .where(Message.session_id == sid)
                     .order_by(Message.created_at.asc())  # Order by creation time ASC
                     .limit(limit))

            # Convert to list of dictionaries
            messages: List[MessageHistory] = []
            for msg in query:
                messages.append(MessageHistory(
                    role=msg.role,
                    content=msg.content,
                    created_at=msg.created_at.isoformat(),
                    session_id=session_id
                ))

            self.logger.info(f"Retrieved {len(messages)} messages for session {sid}")
            return messages
        except Exception as e:
            self.logger.error(f"Error getting messages for session {sid}: {e}")
            self.logger.error(traceback.format_exc())
            return []

    async def save_form_data(
        self,
        form_data: Any,  # Expecting FormData object here
        session_id: Optional[str] = None
    ) -> bool:
        """
        Saves the current state of the form data (as a JSON string) to the database.

        Args:
            form_data: The FormData object containing the current state.
            session_id: The ID of the session. Uses the manager's current session ID if None.

        Returns:
            True if saving was successful, False otherwise.
        """
        sid = session_id or self.session_id
        if not sid:
            self.logger.error("No active session ID provided for save_form_data")
            raise ValueError("No active session")

        try:
            # First output detailed information about what's in form_data
            self.logger.debug(f"Session {sid}: Saving form data. Has user_form: {hasattr(form_data, 'user_form')}")
            if hasattr(form_data, 'user_form') and form_data.user_form is not None:
                self.logger.debug(f"Session {sid}: User form fields: {form_data.user_form.model_fields_set}")

            # Convert form data to dictionary using safe_dict
            data_dict = None
            if hasattr(form_data, "safe_dict"):
                self.logger.debug(f"Session {sid}: Using safe_dict() method")
                data_dict = form_data.safe_dict()
            else:
                self.logger.debug(f"Session {sid}: No safe_dict method, using direct conversion")
                data_dict = form_data

            # Check that form data is correctly saved in the dictionary
            if isinstance(data_dict, dict) and "user_form" in data_dict:
                self.logger.debug(f"Session {sid}: User form in data_dict: {json.dumps(data_dict['user_form'], indent=2, ensure_ascii=False)}")
            else:
                self.logger.warning(f"Session {sid}: Missing user_form in data_dict!")

            # Serialize form data to JSON
            data_json = json.dumps(data_dict, ensure_ascii=False)

            # Output the full data being saved to the database
            self.logger.info(f"Saving form data (dict) for session {sid}: {json.dumps(data_dict, indent=2, ensure_ascii=False)}")

            # Create state in database
            with database.atomic():
                State.create(
                    session_id=sid,
                    data=data_json,
                    created_at=datetime.now()
                )

            self.logger.info(f"Saved form data state for session {sid}")
            return True
        except Exception as e:
            self.logger.error(f"Error saving form data for session {sid}: {e}")
            self.logger.error(traceback.format_exc())
            return False

    async def get_latest_form_data(
        self,
        session_id: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Retrieves the latest saved form data state for a session as a dictionary.

        Args:
            session_id: The ID of the session. Uses the manager's current session ID if None.

        Returns:
            A dictionary representing the latest form data state, or None if not found.
        """
        sid = session_id or self.session_id
        if not sid:
            self.logger.error("No active session ID provided for get_latest_form_data")
            raise ValueError("No active session")

        try:
            # Get latest state from database
            query = (State
                     .select()
                     .where(State.session_id == sid)
                     .order_by(State.created_at.desc())
                     .limit(1))

            # Return state data if found
            state = query.get_or_none()
            if state:
                self.logger.info(f"Retrieved latest form data state for session {sid}")
                return json.loads(state.data)
            else:
                self.logger.info(f"No form data state found for session {sid}")
                return None

        except Exception as e:
            self.logger.error(f"Error getting latest form data for session {sid}: {e}")
            self.logger.error(traceback.format_exc())
            return None

    async def get_session_info(
        self,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Retrieves basic information about a specific session.

        Args:
            session_id: The ID of the session. Uses the manager's current session ID if None.

        Returns:
            A dictionary containing session information, or an empty dict if not found.
        """
        sid = session_id or self.session_id
        if not sid:
            self.logger.error("No active session ID provided for get_session_info")
            raise ValueError("No active session")

        try:
            # Get session from database
            session = Session.get(Session.session_id == sid)

            # Return session information
            session_info_dict = {
                "session_id": session.session_id,
                "user_id": session.user_id,
                "client_id": session.client_id,
                "form_class": session.form_class,
                "created_at": session.created_at.isoformat()
            }
            self.logger.info(f"Retrieved info for session {sid}")
            return session_info_dict
        except DoesNotExist:
            self.logger.error(f"Session not found: {sid}")
            return {}
        except Exception as e:
            self.logger.error(f"Error getting session info for {sid}: {e}")
            self.logger.error(traceback.format_exc())
            return {}
