from flask import Flask

from src.config import FlaskConfig
from src.extensions import db, migrate
from src.routes import register_routes


def create_app() -> Flask:
    """
    Create and configure an instance of a Flask application.

    Returns:
        Flask: A Flask application instance configured with database,
               migration tools, custom routes, and specific configurations.
    """
    app = Flask(__name__)  # Create a Flask application instance
    app.config.from_object(FlaskConfig)  # Load configurations from FlaskConfig
    app.json.sort_keys = False  # Configure JSON responses to not sort keys

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)

    # Create database tables within the application context
    with app.app_context():
        from src.models import user, task, label, history  # Import database models

        db.create_all()  # Create database tables for all models

    # Register custom routes for the application
    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()  # Create a Flask app instance
    app.run(debug=True)  # Run the app with debugging enabled
