# AI Learning & Development Log

## Project: Task Management System

I used AI during the development of this project mainly to understand the flow of the application and to help me with implementation. I did not directly use the generated code without checking it. I implemented the suggestions, tested them locally, and made changes when required.

---

## 1. Project Planning

### What I asked AI
I first wanted to understand how I should structure the Task Management System and how the frontend, backend, API, and database would be connected.

### What AI suggested
AI helped me define the project structure and the flow:

Frontend → Backend/API → Database

It also helped me break the backend into different parts such as routes, models, schemas, and database configuration.

### What I implemented
I first planned the architecture and created the backend structure before starting the frontend.

### What I changed
I used the suggested structure as a starting point and adjusted it according to what I understood from the project.

### What I learned
I understood that I should first think about the complete flow of the application instead of directly starting with individual code files.

---

## 2. Backend Development

### What I asked AI
My main objective was to understand how a REST API works and how the backend connects to the database. I asked AI for help in building the backend using FastAPI, SQLAlchemy, and PostgreSQL.

### What AI suggested
AI suggested creating REST API endpoints for task operations and using SQLAlchemy to communicate with PostgreSQL.

### What I implemented
I built the backend first and connected it to PostgreSQL.

I created the task APIs and tested them using Swagger.

### What I changed
While implementing, I made changes based on the actual project structure and issues I faced while running the application locally.

### What I learned
I understood the backend flow better:

Request → FastAPI → API logic → Database → Response

Testing the APIs through Swagger helped me understand what was actually happening between the API and database.

---

## 3. Frontend Development

### What I asked AI
After I understood the backend flow, I moved to the frontend part. I asked AI how to create the React frontend and connect it with my existing backend APIs.

### What AI suggested
AI suggested using React for the frontend and calling the FastAPI REST APIs from the frontend.

### What I implemented
I created the frontend using React and connected it with the backend.

### What I changed
I adjusted the frontend implementation according to my actual API endpoints and the responses returned by the backend.

### What I learned
I understood how the frontend communicates with the backend through APIs and how the data flows between both sides.

---

## 4. Testing the Complete Application

After connecting the frontend and backend, I ran the complete project locally and manually tested it.

I checked:

- Frontend functionality
- API requests and responses
- Backend behavior
- Database changes
- Frontend and backend communication

If something did not work as expected, I checked the flow and made the required changes.

---

## 5. How My Thinking Improved

The biggest improvement for me was understanding the application as a complete system.

Earlier, I mainly focused on writing code for a particular problem. During this project, I started thinking about:

- How the application should be structured
- How data moves from frontend to backend
- How APIs communicate between components
- How backend code interacts with the database
- How to test each part separately
- How to find where a problem is occurring

I also learned that AI can help with implementation, but I need to understand the code, verify it, test it, and make the final decisions myself.

---

## 6. AI Usage Summary

My development flow was:

**Plan → Build Backend → Connect Database → Test APIs → Understand Backend Flow → Build Frontend → Connect Frontend & Backend → Test Complete Application**

I used ChatGPT mainly for planning, understanding concepts, and creating the initial project structure.

I used Claude mainly during the implementation of the backend and frontend.

I used AI as an assistant, but I verified the implementation by running and testing the project locally.