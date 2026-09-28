"""
models.py
---------
This file defines the actual database table structure using SQLAlchemy's
ORM (Object Relational Mapper). Each class here maps to one table in
PostgreSQL, and each class attribute maps to one column.
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Task(Base):
    """
    Represents a single row in the 'tasks' table.
    """

    __tablename__ = "tasks"

    # Primary key, auto-incrementing integer
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Required short text field
    title = Column(String(255), nullable=False)

    # Optional long text field
    description = Column(Text, nullable=True)

    # Priority is stored as a plain string ("Low" / "Medium" / "High").
    # The allowed values are enforced in the Pydantic schemas, not here,
    # to keep the database layer simple for this educational project.
    priority = Column(String(10), nullable=False, default="Medium")

    # Optional due date (date only, no time component)
    due_date = Column(Date, nullable=True)

    # Whether the task has been completed
    completed = Column(Boolean, nullable=False, default=False)

    # Automatically set by the database when a row is first created
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Automatically updated by the database whenever a row is changed
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
