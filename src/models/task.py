from src.extensions import db
from src.models.associations import task_labels

from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint, String, DateTime
from sqlalchemy.orm import backref, relationship


class Task(db.Model):
    """Model for tasks, including subtasks and labels."""

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)
    status: str = Column(String, nullable=False, default="Pending")
    user_id: int = Column(Integer, ForeignKey("user.id"))
    due_date: DateTime = Column(DateTime)
    parent_id: int = Column(Integer, ForeignKey("task.id"))  # For subtasks

    # Relationships
    subtasks = relationship("Task", backref=backref("parent", remote_side=[id]))
    labels = relationship("Label", secondary=task_labels, back_populates="tasks")

    __table_args__ = (
        CheckConstraint(status.in_(["Pending", "Doing", "Blocked", "Done"])),
    )

    def to_dict(self) -> dict:
        """Convert the Task object to a dictionary representation."""
        due_date_format = (
            self.due_date.strftime("%Y-%m-%d %H:%M:%S") if self.due_date else None
        )
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "user_id": self.user_id,
            "labels": [x.name for x in self.labels],
            "due_date": due_date_format,
            "subtasks": [subtask.to_dict() for subtask in self.subtasks],
        }

    def __repr__(self) -> str:
        """Return a string representation of the task."""
        return f"<Task {self.title}>"
