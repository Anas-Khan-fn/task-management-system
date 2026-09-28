# Task Management System

A full-stack Task Management application built to practice and demonstrate backend, frontend, database, REST API, and software engineering concepts.

The project was developed incrementally, starting with the backend and database, followed by REST API testing, frontend development, and finally connecting the frontend and backend.

## Project Overview

The main goal of this project was to understand how a complete software application works from end to end.

The development flow was:

**Plan Architecture → Build Backend → Connect PostgreSQL → Test REST APIs → Build Frontend → Connect Frontend & Backend → Test Complete Application**

The project contains:

- React frontend
- FastAPI backend
- PostgreSQL database
- REST APIs
- SQLAlchemy ORM
- Swagger/OpenAPI documentation
- Git/GitHub version control

---

# Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL

## Frontend

- React
- JavaScript
- Vite
- CSS
- Axios
- React Router

## Database

- PostgreSQL

## Tools

- Git
- GitHub
- VS Code
- Swagger / OpenAPI

---

# Architecture

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

## Application Flow

```text
User
 │
 ▼
React Frontend
 │
 │ HTTP Request
 ▼
FastAPI REST API
 │
 ▼
SQLAlchemy
 │
 ▼
PostgreSQL
 │
 ▼
FastAPI Response
 │
 ▼
React Frontend
```

---

# Current Features

## Task Management

- Create a task
- View all tasks
- View a task by ID
- Update a task
- Delete a task
- Mark a task as completed
- Mark a task as incomplete
- Set task priority
- Set task due date
- Add task description
- View task status

## Backend

- REST API built with FastAPI
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request/response schemas
- Swagger/OpenAPI API documentation
- CRUD operations
- Complete/incomplete task endpoints
- Health check endpoint

## Frontend

- React-based user interface
- Add new task
- View task list
- Edit task
- Delete task
- Mark task as completed
- Mark task as pending
- Task priority selection
- Task due date
- Task description

---

# REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{task_id}` | Get a single task |
| PUT | `/api/tasks/{task_id}` | Update a task |
| DELETE | `/api/tasks/{task_id}` | Delete a task |
| PATCH | `/api/tasks/{task_id}/complete` | Mark a task as completed |
| PATCH | `/api/tasks/{task_id}/incomplete` | Mark a task as incomplete |
| GET | `/` | Health check |

---

# Project Structure

```text
task-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── tasks.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── TaskList.jsx
│   │   │   ├── AddTask.jsx
│   │   │   └── EditTask.jsx
│   │   │
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── .gitignore
│
├── docs/
│   └── screenshots/
│       ├── task-manager.png
│       └── swagger-api.png
│
├── AI-Learning.md
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Prerequisites

Before installing the project, make sure the following are installed:

- Python
- PostgreSQL
- Node.js and npm
- Git

You can verify the installations using:

```bash
python --version
```

```bash
node --version
```

```bash
npm --version
```

```bash
git --version
```

---

# Backend Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Anas-Khan-fn/task-management-system.git
```

Go into the project:

```bash
cd task-management-system
```

---

## 2. Create a Python Virtual Environment

From the project root:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can allow locally created scripts with:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see `(venv)` at the beginning of the terminal line.

---

## 4. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

The backend uses FastAPI, Uvicorn, SQLAlchemy, PostgreSQL database connectivity, Pydantic, and related dependencies.

---

# PostgreSQL Setup

## 1. Create the Database

Open PostgreSQL using `psql` or pgAdmin and create the database:

```sql
CREATE DATABASE task_management;
```

---

## 2. Configure the Database Connection

Create a `.env` file in the project root.

Add your PostgreSQL connection URL:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/task_management
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password.

**Do not commit `.env` to GitHub.**

The project `.gitignore` already contains:

```text
.env
```

so your database credentials remain outside the repository.

---

# Run the Backend

From the project root, make sure the virtual environment is activated.

Run:

```bash
python -m uvicorn app.main:app --reload
```

The backend will start at:

```text
http://127.0.0.1:8000
```

You should see:

```text
Application startup complete.
```

---

# Swagger API Documentation

FastAPI automatically provides Swagger/OpenAPI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger to test the REST API endpoints directly.

The API documentation includes:

- GET all tasks
- POST create task
- GET task by ID
- PUT update task
- DELETE task
- PATCH complete task
- PATCH incomplete task
- Health check

---

# Backend API Testing Flow

The backend can be tested independently using Swagger.

Recommended testing flow:

### 1. Create a task

Use:

```text
POST /api/tasks/
```

Create a task with a title, description, priority, and due date.

### 2. Get all tasks

Use:

```text
GET /api/tasks/
```

Verify that the created task appears.

### 3. Get a task by ID

Use:

```text
GET /api/tasks/{task_id}
```

Enter the ID of an existing task.

### 4. Update a task

Use:

```text
PUT /api/tasks/{task_id}
```

Change the task information and verify the response.

### 5. Mark the task as completed

Use:

```text
PATCH /api/tasks/{task_id}/complete
```

Verify that the task status changes to completed.

### 6. Mark the task as incomplete

Use:

```text
PATCH /api/tasks/{task_id}/incomplete
```

Verify that the task becomes pending/incomplete again.

### 7. Delete the task

Use:

```text
DELETE /api/tasks/{task_id}
```

Then call:

```text
GET /api/tasks/
```

to verify that the task has been removed.

---

# Frontend Installation

The frontend is located inside the `frontend` directory.

## 1. Open the Frontend Directory

From the project root:

```bash
cd frontend
```

---

## 2. Install Frontend Dependencies

Run:

```bash
npm install
```

This installs the dependencies defined in `package.json`.

---

## 3. Configure the Backend API URL

The frontend communicates with the FastAPI backend through the API URL.

The local backend API is:

```text
http://127.0.0.1:8000/api
```

If the frontend uses a `.env` file, the API URL can be configured as:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

---

# Run the Frontend

Make sure the backend is already running.

From the `frontend` directory:

```bash
npm run dev
```

Vite will provide a local URL, normally:

```text
http://localhost:5173
```

Open the URL in your browser.

---

# Running the Complete Application

You need to run both the backend and frontend.

## Terminal 1 — Backend

From the project root:

```bash
.\venv\Scripts\Activate.ps1
```

Then:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Terminal 2 — Frontend

Open another terminal.

Go to the frontend:

```bash
cd frontend
```

Then:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

The complete flow is:

```text
React Frontend
      ↓
HTTP Request
      ↓
FastAPI Backend
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
Response
      ↓
React Frontend
```

---

# Frontend Testing

The complete application can be tested through the React interface.

### Create

Click:

```text
+ Add New Task
```

Fill in:

- Title
- Description
- Priority
- Due Date

Click:

```text
Create Task
```

The task should appear in the task list.

### Read

Refresh the browser.

The task should still be available because the data is stored in PostgreSQL.

### Update

Click:

```text
Edit
```

Change the task information and save the changes.

Verify that the updated information appears in the task list.

### Complete

Click:

```text
Complete
```

The task status should change to:

```text
Completed
```

The button changes to:

```text
Mark Pending
```

### Mark Pending

Click:

```text
Mark Pending
```

The task should return to the pending state.

### Delete

Click:

```text
Delete
```

Confirm the deletion.

The task should disappear from the task list.

---

# Screenshots

## Task Management Frontend

The React frontend provides the interface for creating, viewing, updating, and completing tasks.

![Task Management Frontend](docs/screenshots/task-manager.png)

## REST API - Swagger Documentation

The FastAPI backend provides REST APIs for task management and can be tested using Swagger/OpenAPI.

![Swagger API Documentation](docs/screenshots/swagger-api.png)

---

# Database

The application uses PostgreSQL for persistent task storage.

The backend uses SQLAlchemy to communicate with PostgreSQL.

The general database flow is:

```text
FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL
```

This allows task data to remain available even after refreshing or restarting the frontend.

---

# Git and GitHub

Git is used for version control and GitHub is used to store the project repository.

Repository:

https://github.com/Anas-Khan-fn/task-management-system

Basic workflow:

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "Describe the change"
```

```bash
git push
```

The project also uses `.gitignore` to prevent files such as `.env`, Python cache files, and the virtual environment from being committed.

---

# AI-Assisted Development

AI was used as an assistant during the development of this project.

The development process started with planning the project architecture and understanding how the different components would work together.

### ChatGPT

ChatGPT was mainly used for:

- Understanding project requirements
- Planning the project architecture
- Understanding REST API concepts
- Creating the initial project structure
- Discussing implementation approaches
- Understanding backend and frontend flow

### Claude

Claude was mainly used during implementation for:

- Backend development
- FastAPI implementation
- Database integration
- React frontend development
- Frontend and backend integration

AI suggestions were reviewed, implemented, tested locally, and changed when required.

The detailed AI development process is documented in:

```text
AI-Learning.md
```

The document records:

- What I asked AI
- What AI suggested
- What I implemented
- What I changed
- How I tested the implementation
- What I learned
- How my thinking improved as a software engineer

---

# What I Learned

The project helped me understand the complete flow of a full-stack application.

Some of the main concepts I learned through implementation were:

- REST APIs
- HTTP request and response flow
- FastAPI
- SQLAlchemy
- PostgreSQL
- CRUD operations
- API request/response schemas
- Swagger/OpenAPI
- React frontend
- Frontend/backend communication
- Database integration
- Git and GitHub
- Local application testing
- Debugging by checking different layers of the application

One of the main things I learned was to think about the complete flow instead of only individual pieces of code.

For example:

```text
User
 ↓
Frontend
 ↓
API
 ↓
Backend
 ↓
Database
 ↓
Backend
 ↓
API Response
 ↓
Frontend
```

---

# Development Approach

I developed the project incrementally.

### Phase 1 — Planning

I first planned the architecture and project structure.

### Phase 2 — Backend

I built the FastAPI backend and REST API endpoints.

### Phase 3 — Database

I connected the backend to PostgreSQL using SQLAlchemy.

### Phase 4 — API Testing

I tested the REST APIs using Swagger.

### Phase 5 — Frontend

After understanding the backend flow, I created the React frontend.

### Phase 6 — Integration

I connected the React frontend with the FastAPI backend.

### Phase 7 — End-to-End Testing

I ran the complete application locally and manually tested the functionality.

---

# Project Status

**Active Development**

The project is being developed incrementally.

Future improvements may include additional validation, authentication, automated testing, better error handling, deployment, containerization, and other software engineering practices.

---

# Author

**Anas Khan**

GitHub:

https://github.com/Anas-Khan-fn
