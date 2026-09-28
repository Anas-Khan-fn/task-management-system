"""
main.py
-------
This is the entry point of the application. Running:

    uvicorn app.main:app --reload

starts this file, which:
  1. Creates the FastAPI app.
  2. Creates the database tables (if they don't already exist).
  3. Registers the task routes.
  4. Enables CORS so a React frontend can call this API later.
  5. Adds a simple root endpoint to confirm the server is alive.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app.routes import tasks

# Create all tables defined in models.py, if they don't exist yet.
# For this educational project we use this instead of a migration tool.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="A simple educational Task Management REST API built with FastAPI, SQLAlchemy, and PostgreSQL.",
    version="1.0.0",
)

# Allow a React dev server (Vite default ports) to call this API from
# the browser without being blocked by CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routes defined in routes/tasks.py
app.include_router(tasks.router)


@app.get("/", summary="Health check")
def read_root():
    return {"message": "Task Management API is running"}
