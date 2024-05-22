import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()


class FlaskConfig:
    """Configuration class for Flask application."""

    # URI for the SQLAlchemy database
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")

    # Flag to track modifications of SQLAlchemy objects
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = (
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS") == "True"
    )

    # Secret key for session management and other secrets
    SECRET_KEY: str = os.getenv("SECRET_KEY")


# URL for the Flask application
FLASK_URL: str = os.getenv("FLASK_URL")
