# Task Manager — Frontend

A simple React + Vite + Tailwind CSS frontend for the Task Management API, using Axios and React Router.

## 1. Installation (Windows)

If you're starting from scratch:

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install axios react-router-dom
npm install -D tailwindcss @tailwindcss/vite
```

If you're using the files provided here, just run:

```bash
cd frontend
npm install
```

## 2. Configure the API URL

The `.env` file already contains:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

Change this if your backend runs somewhere else.

## 3. Running

Start the backend first (in the backend project folder):

```bash
uvicorn app.main:app --reload
```

Then start the frontend:

```bash
npm run dev
```

Open:

```text
http://localhost:5173
```

Backend Swagger docs (for reference):

```text
http://127.0.0.1:8000/docs
```

## 4. Testing the Full Application

1. **Create** — Task Manager → "+ Add New Task" → fill the form → "Create Task". Confirm the task appears on the list.
2. **Read** — Refresh the browser. The task should still be there — this proves it's coming from PostgreSQL, not local state.
3. **Update** — Click "Edit" on a task → change the title → "Update Task". Confirm the change shows on the list.
4. **Complete** — Click "Complete". Confirm the card now shows "Status: Completed" and the button changes to "Mark Pending".
5. **Mark Pending** — Click "Mark Pending". Confirm it goes back to "Status: Pending".
6. **Delete** — Click "Delete" → confirm the browser prompt. Confirm the task disappears from the list.

## Project Structure

```text
frontend/
│
├── src/
│   ├── pages/
│   │   ├── TaskList.jsx
│   │   ├── AddTask.jsx
│   │   └── EditTask.jsx
│   │
│   ├── api.js
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── .env
├── .gitignore
├── index.html
├── vite.config.js
├── package.json
└── README.md
```
