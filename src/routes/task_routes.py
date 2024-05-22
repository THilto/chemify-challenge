from datetime import datetime

from src.extensions import db
from src.models.history import TaskHistory
from src.models.task import Task

from flask import Blueprint, request, jsonify, Response


# Create a Blueprint for task-related routes
task_blueprint = Blueprint("tasks", __name__)


@task_blueprint.route("/users/<int:user_id>/tasks/", methods=["POST"])
def add_task(user_id: int) -> tuple[dict, int]:
    """Add a new task for the specified user."""
    data = request.get_json()
    due_date = datetime.fromisoformat(data["due_date"])
    new_task = Task(
        title=data["title"],
        user_id=user_id,
        description=data["description"],
        due_date=due_date,
        status="Pending",
    )
    db.session.add(new_task)
    db.session.commit()
    return {"message": "Task Added"}, 200


@task_blueprint.route("/users/<int:user_id>/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(user_id: int, task_id: int) -> tuple[dict, int]:
    """Delete a task for the specified user and task ID, moving it to history."""
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


@task_blueprint.route("/users/<int:user_id>/tasks/<int:task_id>", methods=["PUT"])
def update_task(user_id: int, task_id: int) -> tuple[dict, int]:
    """Update a task for the specified user and task ID."""
    data = request.get_json()
    task = Task.query.filter_by(id=task_id, user_id=user_id).first()
    if not task:
        return {"error": "Task not found"}, 404

    task.title = data["title"] if data["title"] != "" else task.title
    task.description = (
        data["description"] if data["description"] != "" else task.description
    )
    task.status = data["status"] if data["status"] != "" else task.status
    task.due_date = (
        datetime.fromisoformat(data["due_date"])
        if data["due_date"] != ""
        else task.due_date
    )

    db.session.commit()
    return {"message": "Task Updated"}, 200


@task_blueprint.route("/users/<int:user_id>/tasks", methods=["GET"])
def get_tasks(user_id: int) -> tuple[Response, int]:
    """Retrieve all tasks for the specified user."""
    tasks = Task.query.filter_by(user_id=user_id, parent_id=None).all()
    tasks_dict = [task.to_dict() for task in tasks]
    return jsonify(tasks_dict), 200
