from flask import Blueprint, request

from src.extensions import db
from src.models.label import Label
from src.models.task import Task

# Create a Blueprint for label-related routes
label_blueprint = Blueprint("labels", __name__)


@label_blueprint.route(
    "/users/<int:user_id>/tasks/<int:task_id>/labels", methods=["POST"]
)
def add_label_to_task(user_id: int, task_id: int) -> tuple[dict, int]:
    """Add a label to a specific task for the specified user."""
    data = request.get_json()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return {"error": "Task not found"}, 404

    # Check if the label already exists, otherwise create a new one
    label = Label.query.filter_by(name=data["label"]).first()
    if not label:
        label = Label(name=data["label"])
        db.session.add(label)

    # Append the label to the task's labels
    task.labels.append(label)
    db.session.commit()
    return {"message": "Label added to task"}, 200
