import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api.js";

function formatDate(dateString) {
  if (!dateString) return null;
  const date = new Date(dateString);
  return date.toLocaleDateString("en-GB", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Fetch all tasks from the backend when the page first loads
  useEffect(() => {
    fetchTasks();
  }, []);

  function fetchTasks() {
    setLoading(true);
    setError("");

    api
      .get("/tasks/")
      .then((response) => {
        setTasks(response.data);
      })
      .catch(() => {
        setError("Failed to load tasks.");
      })
      .finally(() => {
        setLoading(false);
      });
  }

  function handleToggleComplete(task) {
    const endpoint = task.completed
      ? `/tasks/${task.id}/incomplete`
      : `/tasks/${task.id}/complete`;

    api
      .patch(endpoint)
      .then((response) => {
        // Replace just this one task in the list with the updated version
        setTasks((prevTasks) =>
          prevTasks.map((t) => (t.id === task.id ? response.data : t))
        );
      })
      .catch(() => {
        setError("Failed to update task status.");
      });
  }

  function handleDelete(taskId) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (!confirmed) return;

    api
      .delete(`/tasks/${taskId}`)
      .then(() => {
        setTasks((prevTasks) => prevTasks.filter((t) => t.id !== taskId));
      })
      .catch(() => {
        setError("Failed to delete task.");
      });
  }

  return (
    <div className="min-h-screen bg-gray-100 py-10 px-4">
      <div className="max-w-2xl mx-auto">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-2xl font-semibold text-gray-800">
            Task Manager
          </h1>
          <Link
            to="/add"
            className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
          >
            + Add New Task
          </Link>
        </div>

        {loading && <p className="text-gray-600">Loading tasks...</p>}

        {!loading && error && <p className="text-red-600">{error}</p>}

        {!loading && !error && tasks.length === 0 && (
          <div className="bg-white border border-gray-200 rounded p-6 text-center">
            <p className="text-gray-600 mb-4">No tasks found.</p>
            <Link
              to="/add"
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
            >
              Add Your First Task
            </Link>
          </div>
        )}

        {!loading && !error && tasks.length > 0 && (
          <div className="space-y-4">
            {tasks.map((task) => (
              <div
                key={task.id}
                className="bg-white border border-gray-200 rounded p-4"
              >
                <h2 className="text-lg font-medium text-gray-800">
                  {task.title}
                </h2>

                {task.description && (
                  <p className="text-gray-600 mt-1">{task.description}</p>
                )}

                <div className="mt-2 text-sm text-gray-700 space-y-1">
                  <p>Priority: {task.priority}</p>
                  {task.due_date && (
                    <p>Due Date: {formatDate(task.due_date)}</p>
                  )}
                  <p>Status: {task.completed ? "Completed" : "Pending"}</p>
                </div>

                <div className="mt-4 flex gap-2">
                  <button
                    onClick={() => handleToggleComplete(task)}
                    className="bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded text-sm"
                  >
                    {task.completed ? "Mark Pending" : "Complete"}
                  </button>

                  <Link
                    to={`/edit/${task.id}`}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1.5 rounded text-sm"
                  >
                    Edit
                  </Link>

                  <button
                    onClick={() => handleDelete(task.id)}
                    className="bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded text-sm"
                  >
                    Delete
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export default TaskList;
