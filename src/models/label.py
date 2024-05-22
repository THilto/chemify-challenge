from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.extensions import db
from src.models.associations import task_labels


class Label(db.Model):
    """Model for labels that can be assigned to tasks."""

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False, unique=True)
    tasks = relationship("Task", secondary=task_labels, back_populates="labels")

    def __repr__(self) -> str:
        """Return a string representation of the label."""
        return f"<Label {self.name}>"
