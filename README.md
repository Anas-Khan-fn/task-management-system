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

But the closing **three backticks are missing or misplaced** before `## Screenshots`.

---

## Fix it

Your README should have this structure:

````markdown
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
```

## Screenshots

### Task Management Frontend

The React frontend provides the interface for creating, viewing, updating, and completing tasks.

![Task Management Frontend](https://github.com/user-attachments/assets/40612e5f-10bd-47f3-96b1-2a170df73561)

### REST API - Swagger Documentation

The FastAPI backend provides REST APIs for task management. The APIs can be tested using Swagger/OpenAPI documentation.

![Swagger API Documentation](https://github.com/user-attachments/assets/3b1c87ba-2983-4839-991f-ce6bf4cf755c)
