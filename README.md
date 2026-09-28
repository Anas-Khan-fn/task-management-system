# Task Management API

A simple educational Task Management REST API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## 1. Create the PostgreSQL Database

Open `psql` (or pgAdmin) and run:

```sql
CREATE DATABASE task_management;
```

## 2. Create a Virtual Environment

From the project root (`task-management-backend/`):

```bash
python -m venv venv
```

## 3. Activate It (Windows)

```bash
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your terminal line.

## 4. Install Requirements

```bash
pip install -r requirements.txt
```

## 5. Configure `.env`

Copy `.env.example` to a new file named `.env`:

```bash
copy .env.example .env
```

Open `.env` and replace `YOUR_PASSWORD` with your actual PostgreSQL password:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/task_management
```

**Never commit `.env` to Git** — it's already listed in `.gitignore`.

## 6. Start the FastAPI Server

```bash
uvicorn app.main:app --reload
```

You should see output ending with something like:

```text
Application startup complete.
```

This also automatically creates the `tasks` table in PostgreSQL if it doesn't exist yet.

## 7. Open Swagger

Visit:

```text
http://127.0.0.1:8000/docs
```

ReDoc is also available at:

```text
http://127.0.0.1:8000/redoc
```

## 8. Test Every Endpoint

Follow this sequence inside Swagger UI:

1. **POST /api/tasks/** — click "Try it out", create at least 2 tasks with different titles/priorities.
2. **GET /api/tasks/** — confirm both tasks appear in the list.
3. **GET /api/tasks/{task_id}** — enter one task's id, confirm it returns that single task.
4. **PUT /api/tasks/{task_id}** — change the title and/or priority, confirm the response reflects the update.
5. **PATCH /api/tasks/{task_id}/complete** — confirm `completed` becomes `true`.
6. **PATCH /api/tasks/{task_id}/incomplete** — confirm `completed` becomes `false` again.
7. **DELETE /api/tasks/{task_id}** — delete one task, then call **GET /api/tasks/** again and confirm it's gone.

## Project Structure

```text
task-management-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       └── tasks.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
