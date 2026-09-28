"""
schemas.py
----------
This file defines the Pydantic "schemas". These control:
  - what shape of data the API will ACCEPT (request bodies), and
  - what shape of data the API will RETURN (response bodies).

FastAPI uses these automatically to validate incoming requests and to
generate the Swagger (/docs) documentation.

Note the difference between models.py and schemas.py:
  - models.py  -> describes the PostgreSQL table (SQLAlchemy)
  - schemas.py -> describes the JSON going in/out of the API (Pydantic)
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class PriorityEnum(str, Enum):
    """Restricts the 'priority' field to exactly these three values."""
    low = "Low"
    medium = "Medium"
    high = "High"


class TaskCreate(BaseModel):
    """Schema used when creating a new task (POST /api/tasks)."""

    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    priority: PriorityEnum = PriorityEnum.medium
    due_date: Optional[date] = None


class TaskUpdate(BaseModel):
    """
    Schema used when updating a task (PUT /api/tasks/{task_id}).
    Every field is optional, since an update might only change one thing.
    """

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    priority: Optional[PriorityEnum] = None
    due_date: Optional[date] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    """
    Schema used when sending a task back to the client.
    `model_config` with `from_attributes=True` allows Pydantic to read
    values directly off a SQLAlchemy model object (e.g. task.title)
    instead of requiring a plain dictionary.
    """

    id: int
    title: str
    description: Optional[str] = None
    priority: str
    due_date: Optional[date] = None
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
