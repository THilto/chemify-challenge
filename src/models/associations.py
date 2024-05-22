from sqlalchemy import Table, Column, Integer, ForeignKey

from src.extensions import db


# Association table for many-to-many relationship between tasks and labels
task_labels: Table = Table(
    "task_labels",
    db.metadata,
    Column("task_id", Integer, ForeignKey("task.id"), primary_key=True),
    Column("label_id", Integer, ForeignKey("label.id"), primary_key=True),
)
