from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from src.extensions import db


class TaskHistory(db.Model):
    """Model for storing task history records, including deleted and restored tasks."""

    id: int = Column(Integer, primary_key=True)
    task_id: int = Column(Integer, nullable=False)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    status: str = Column(String, nullable=False)
    user_id: int = Column(Integer, nullable=False)
    due_date: DateTime = Column(DateTime)
    deleted_at: DateTime = Column(DateTime, default=datetime.utcnow)
    restored: bool = Column(Boolean, default=False)

    def to_dict(self) -> dict:
        """Convert the TaskHistory object to a dictionary representation."""
        return {
            "id": self.id,
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "user_id": self.user_id,
            "due_date": (
                self.due_date.strftime("%Y-%m-%d %H:%M:%S") if self.due_date else None
            ),
            "deleted_at": self.deleted_at.strftime("%Y-%m-%d %H:%M:%S"),
            "restored": self.restored,
        }

    def __repr__(self) -> str:
        """Return a string representation of the task history record."""
        return f"<TaskHistory {self.title}>"
