import { useEffect, useState } from "react";
import { useNavigate, useParams, Link } from "react-router-dom";
import api from "../api.js";

function EditTask() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState("Medium");
  const [dueDate, setDueDate] = useState("");
  const [completed, setCompleted] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Load the existing task's data so the form can be pre-filled
  useEffect(() => {
    api
      .get(`/tasks/${id}`)
      .then((response) => {
        const task = response.data;
        setTitle(task.title);
        setDescription(task.description || "");
        setPriority(task.priority);
        setDueDate(task.due_date || "");
        setCompleted(task.completed);
      })
      .catch(() => {
        setError("Failed to load task.");
      })
      .finally(() => {
        setLoading(false);
      });
  }, [id]);

  function handleSubmit(e) {
    e.preventDefault();
    setError("");

    api
      .put(`/tasks/${id}`, {
        title,
        description: description || null,
        priority,
        due_date: dueDate || null,
        completed,
      })
      .then(() => {
        navigate("/");
      })
      .catch(() => {
        setError("Failed to update task.");
      });
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-100 py-10 px-4">
        <div className="max-w-lg mx-auto">
          <p className="text-gray-600">Loading tasks...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-100 py-10 px-4">
      <div className="max-w-lg mx-auto bg-white border border-gray-200 rounded p-6">
        <h1 className="text-2xl font-semibold text-gray-800 mb-6">
          Edit Task
        </h1>

        {error && <p className="text-red-600 mb-4">{error}</p>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Title
            </label>
            <input
              type="text"
              required
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full border border-gray-300 rounded px-3 py-2"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              rows={3}
              className="w-full border border-gray-300 rounded px-3 py-2"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Priority
            </label>
            <select
              value={priority}
              onChange={(e) => setPriority(e.target.value)}
              className="w-full border border-gray-300 rounded px-3 py-2"
            >
              <option value="Low">Low</option>
              <option value="Medium">Medium</option>
              <option value="High">High</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Due Date
            </label>
            <input
              type="date"
              value={dueDate}
              onChange={(e) => setDueDate(e.target.value)}
              className="w-full border border-gray-300 rounded px-3 py-2"
            />
          </div>

          <div className="flex gap-2 pt-2">
            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
            >
              Update Task
            </button>
            <Link
              to="/"
              className="bg-gray-200 hover:bg-gray-300 text-gray-800 px-4 py-2 rounded"
            >
              Cancel
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default EditTask;
