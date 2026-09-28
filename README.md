# Task Management System

A full-stack Task Management application built to practice and demonstrate backend, frontend, database, and software engineering concepts.

The project is being developed incrementally, with new features, improvements, testing, and engineering practices being added over time.

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

### Frontend
- React
- JavaScript
- Vite
- CSS

### Database
- PostgreSQL

### Tools
- Git
- GitHub
- VS Code
- Swagger / OpenAPI

## Current Features

- Create tasks
- View all tasks
- View a task by ID
- Update tasks
- Delete tasks
- Mark tasks as completed
- Mark tasks as incomplete
- REST API documentation with Swagger UI
- PostgreSQL database integration
- React frontend

## Architecture

```text
                ┌─────────────────┐
                │  React Frontend │
                └────────┬────────┘
                         │
                         │ HTTP / REST API
                         ▼
                ┌─────────────────┐
                │ FastAPI Backend │
                └────────┬────────┘
                         │
                         │ SQLAlchemy
                         ▼
                ┌─────────────────┐
                │   PostgreSQL    │
                └─────────────────┘
```text
architecture diagram
```

