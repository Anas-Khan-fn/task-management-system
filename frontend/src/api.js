import axios from "axios";

// One Axios instance shared by the whole app.
// The base URL comes from .env (VITE_API_URL), so it's easy to change
// without touching any component code.
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default api;
