from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.extensions import db


class User(db.Model):
    """Model for user accounts."""

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, unique=True, nullable=False)
    tasks = relationship("Task", backref="user")

    def __repr__(self) -> str:
        """Return a string representation of the user."""
        return f"<User {self.username}>"
