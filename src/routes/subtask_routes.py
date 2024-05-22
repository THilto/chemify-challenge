from datetime import datetime

from src.extensions import db
from src.models.task import Task

from flask import Blueprint, request, jsonify

# Create a Blueprint for subtask-related routes
subtask_blueprint = Blueprint("subtasks", __name__)


@subtask_blueprint.route(
    "/users/<int:user_id>/tasks/<int:task_id>/subtasks", methods=["GET"]
)
def get_subtasks(user_id: int, task_id: int) -> tuple:
    """Retrieve all subtasks for a specific parent task."""
    parent_task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not parent_task:
        return {"error": "Parent task not found"}, 404

    subtasks = Task.query.filter_by(parent_id=task_id).all()
    return jsonify([subtask.to_dict() for subtask in subtasks]), 200


@subtask_blueprint.route(
    "/users/<int:user_id>/tasks/<int:task_id>/subtasks", methods=["POST"]
)
def add_subtask(user_id: int, task_id: int) -> tuple[dict, int]:
    """Add a new subtask to a specific parent task."""
    data = request.get_json()
    due_date = datetime.fromisoformat(data["due_date"])

    parent_task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not parent_task:
        return {"error": "Parent task not found"}, 404

    new_subtask = Task(
        title=data["title"],
        user_id=user_id,
        description=data["description"],
        due_date=due_date,
        status="Pending",
        parent_id=parent_task.id,
    )
    db.session.add(new_subtask)
    db.session.commit()
    return {"message": "Subtask added"}, 200
