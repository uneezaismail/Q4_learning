#  Task Tracker API

A simple and minimal task tracking API built using **FastAPI**. This project allows users to create accounts and manage their tasks, with in-memory storage using Python dictionaries.

---

##  Features

-  Create and retrieve users
-  Create, view, and update tasks
-  Validates due dates to be today or later
-  Update task status (pending, in-progress, completed)
-  List all tasks by user
-  Full input validation using **Pydantic**
-  Interactive API docs via Swagger at `/docs`

---

##  Tech Stack

- **FastAPI** – Web framework
- **Pydantic** – Data validation
- **uv** – Package Manager

---

##  API Endpoints

###  Users

| Method | Endpoint                 | Description          |
|--------|--------------------------|----------------------|
| POST   | `/users/`                | Create a new user    |
| GET    | `/users/{user_id}`       | Get user by ID       |
| GET    | `/users/{user_id}/tasks` | List all user tasks  |

###  Tasks

| Method | Endpoint                | Description             |
|--------|-------------------------|-------------------------|
| POST   | `/tasks/`               | Create a new task       |
| GET    | `/tasks/{task_id}`      | Get task by ID          |
| PUT    | `/tasks/{task_id}`      | Update status of a task |

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/uneezaismail/task_tracker_api.git
cd task_tracker_api
```

### 2. Initialize and Set Up the Environment

```bash
uv init fastdca_p1
cd fastdca_p1
uv venv
source .venv/bin/activate  
uv add "fastapi[standard]"
```

### 3. Run the App

```bash
Fastapi dev main.py
```