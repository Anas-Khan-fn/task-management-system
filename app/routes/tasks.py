"""
routes/tasks.py
---------------
This file defines every API endpoint related to tasks. Each function
below is a "route" -- a piece of code that runs when a specific
HTTP method + URL combination is requested (e.g. GET /api/tasks).

Flow for every route:
  1. FastAPI receives the HTTP request.
  2. It validates the request body (if any) against a Pydantic schema.
  3. `Depends(get_db)` gives the route a database session.
  4. The route uses SQLAlchemy to read/write data in PostgreSQL.
  5. The route returns data, which FastAPI converts into JSON using
     the `response_model` schema.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(
    prefix="/api/tasks",
    tags=["Tasks"],
)


def get_task_or_404(task_id: int, db: Session) -> Task:
    """
    Small helper used by several routes below: looks up a task by id,
    and raises a 404 error automatically if it isn't found. This avoids
    repeating the same "check if it exists" code in every route.
    """
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task",
    description="Creates a new task and stores it in PostgreSQL.",
)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    # Convert the validated Pydantic object into a SQLAlchemy model instance
    new_task = Task(
        title=task_in.title,
        description=task_in.description,
        priority=task_in.priority.value,
        due_date=task_in.due_date,
    )

    db.add(new_task)      # stage the new row for insertion
    db.commit()            # actually write it to PostgreSQL
    db.refresh(new_task)   # reload it so we get the DB-generated id/timestamps

    return new_task


@router.get(
    "/",
    response_model=List[TaskResponse],
    summary="Get all tasks",
    description="Returns every task currently stored in the database.",
)
def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).order_by(Task.id).all()
    return tasks


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Get a single task",
    description="Returns one task by its id, or 404 if it doesn't exist.",
)
def get_task(task_id: int, db: Session = Depends(get_db)):
    return get_task_or_404(task_id, db)


@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Update a task",
    description="Updates an existing task. Only fields you include are changed.",
)
def update_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)

    # `exclude_unset=True` means: only include fields the client actually
    # sent in the request body, so we don't accidentally overwrite fields
    # with None.
    update_data = task_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        # priority arrives as a PriorityEnum member; store its plain string
        if field == "priority" and value is not None:
            value = value.value if hasattr(value, "value") else value
        setattr(task, field, value)

    db.commit()
    db.refresh(task)
    return task


@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse,
    summary="Mark a task as completed",
    description="Sets completed = true for the given task.",
)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)
    task.completed = True
    db.commit()
    db.refresh(task)
    return task


@router.patch(
    "/{task_id}/incomplete",
    response_model=TaskResponse,
    summary="Mark a task as incomplete",
    description="Sets completed = false for the given task.",
)
def incomplete_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)
    task.completed = False
    db.commit()
    db.refresh(task)
    return task


@router.delete(
    "/{task_id}",
    summary="Delete a task",
    description="Permanently deletes a task from PostgreSQL.",
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_or_404(task_id, db)
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
