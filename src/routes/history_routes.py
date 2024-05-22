from datetime import datetime

from flask import Blueprint

from src.extensions import db
from src.models.history import TaskHistory
from src.models.task import Task


# Create a Blueprint for history-related routes
history_blueprint = Blueprint("history", __name__)


@history_blueprint.route("/users/<int:user_id>/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(user_id: int, task_id: int) -> tuple[dict, int]:
    """Delete a task for the specified user and task ID, and move it to history."""
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return {"message": "Task not found"}, 404

    # Add a history record
    history_record = TaskHistory(
        task_id=task.id,
        title=task.title,
        description=task.description,
        status=task.status,
        user_id=task.user_id,
        due_date=task.due_date,
        deleted_at=datetime.utcnow(),
        restored=False,
    )
    db.session.add(history_record)
    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted and moved to history"}, 200


@history_blueprint.route(
    "/users/<int:user_id>/tasks/<int:task_id>/restore", methods=["POST"]
)
def restore_task(user_id: int, task_id: int) -> tuple[dict, int]:
    """Restore a deleted task for the specified user and task ID."""
    task_history = TaskHistory.query.filter_by(
        task_id=task_id, user_id=user_id, restored=False
    ).first()
    if not task_history or task_history.restored:
        return {"error": "Task history not found or already restored"}, 404

    # Create a new task from the history record
    restored_task = Task(
        title=task_history.title,
        description=task_history.description,
        status=task_history.status,
        user_id=task_history.user_id,
        due_date=task_history.due_date,
    )
    db.session.add(restored_task)
    task_history.restored = True
    db.session.commit()
    return {"message": "Task restored"}, 200
