# ✅ Task Manager API

A simple and clean task management backend API built with FastAPI and PostgreSQL.

---

## 🚀 What This Project Does

Task Manager lets users:
- Register and login securely
- Create tasks with title, description, priority and due date
- View all their tasks
- Filter tasks by completion status or priority level
- Update any field of a task (partial updates supported)
- Delete tasks
- Track when each task was created

---

## 🧠 What I Learned Building This

- Full CRUD operations (Create, Read, Update, Delete)
- Partial updates using Optional fields in Pydantic
- Query parameters for filtering data
- Python Enum for fixed value choices (low/medium/high)
- Reusing authentication patterns from previous project
- How 60% of every backend project follows the same structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.14 | Programming language |
| FastAPI | Web framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| PyJWT | JWT authentication |
| bcrypt | Password hashing |
| Uvicorn | ASGI server |
| Postman | API testing |

---

## ⚙️ How To Run This Project

### 1. Clone the repository
```bash
git clone https://github.com/sivamani151dev-cell/task-manager.git
cd task-manager
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file:

DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/taskmanager
SECRET_KEY=yoursecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 5. Run database migrations
```bash
python -m alembic upgrade head
```

### 6. Start the server
```bash
uvicorn app.main:app --reload
```

Server runs at `http://127.0.0.1:8000`
API docs at `http://127.0.0.1:8000/docs`

---

## 📡 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/auth/register` | Register new user | ❌ |
| POST | `/auth/login` | Login and get JWT token | ❌ |

### Tasks
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/tasks/` | Create new task | ✅ |
| GET | `/tasks/` | Get all tasks (with filters) | ✅ |
| GET | `/tasks/{task_id}` | Get specific task | ✅ |
| PUT | `/tasks/{task_id}` | Update task (partial) | ✅ |
| DELETE | `/tasks/{task_id}` | Delete task | ✅ |

### Query Parameters for GET /tasks/
| Parameter | Type | Example |
|-----------|------|---------|
| `completed` | boolean | `?completed=true` |
| `priority` | enum | `?priority=high` |

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | Secret key for JWT signing |
| `ALGORITHM` | JWT algorithm (HS256) |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time |

---

## 📁 Project Structure

task-manager/
├── app/
│ ├── main.py # App entry point
│ ├── database.py # Database connection
│ ├── auth.py # JWT and password logic
│ ├── models/
│ │ ├── user.py # User model
│ │ └── task.py # Task model with priority enum
│ ├── schemas/
│ │ ├── user.py # User schemas
│ │ └── task.py # Task schemas with Optional fields
│ └── routers/
│ ├── auth.py # Auth endpoints
│ └── tasks.py # Task CRUD endpoints
├── alembic/ # Database migrations
├── .env.example # Environment variables template
├── requirements.txt # Dependencies
└── README.md # This file

---

## 🎯 Project Type
Learning Project — built to understand full CRUD operations and query parameter filtering.