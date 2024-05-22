from flask import Flask
from .task_routes import task_blueprint
from .subtask_routes import subtask_blueprint
from .history_routes import history_blueprint
from .label_routes import label_blueprint


def register_routes(app: Flask) -> None:
    """Register all blueprints with the given Flask application."""
    app.register_blueprint(task_blueprint)
    app.register_blueprint(subtask_blueprint)
    app.register_blueprint(history_blueprint)
    app.register_blueprint(label_blueprint)
