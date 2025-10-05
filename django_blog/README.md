#  Task Management API


The task Management API is a simple backend application built with **Django REST Framework** that allows users to manage tasks (like a to-do list).  
Users can create, read, update, and delete tasks, as well as mark them as complete or incomplete.

This project is part of my **Capstone Project (Part 3: Build Phase)**.

---

## Features
- CRUD operations for **Users** and **Tasks**
- Mark tasks as **complete/incomplete**
- Simple and clean RESTful API design
- Built with **Django ORM** and **Django REST Framework**
- Ready for deployment on **Heroku** or **PythonAnywhere**

---

##  API Endpoints

### User Endpoints
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/users/` | Create a new user |
| GET | `/api/users/` | List all users |
| GET | `/api/users/{id}/` | Retrieve a single user |
| PUT | `/api/users/{id}/` | Update a user |
| DELETE | `/api/users/{id}/` | Delete a user |

### Task Endpoints
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/` | List all tasks |
| GET | `/api/tasks/{id}/` | Retrieve a specific task |
| PUT | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |
| PATCH | `/api/tasks/{id}/complete/` | Mark task as complete/incomplete |

---

##  Database Design (ERD)
