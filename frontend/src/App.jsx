import { Routes, Route } from "react-router-dom";
import TaskList from "./pages/TaskList.jsx";
import AddTask from "./pages/AddTask.jsx";
import EditTask from "./pages/EditTask.jsx";

function App() {
  return (
    <Routes>
      <Route path="/" element={<TaskList />} />
      <Route path="/add" element={<AddTask />} />
      <Route path="/edit/:id" element={<EditTask />} />
    </Routes>
  );
}

export default App;
