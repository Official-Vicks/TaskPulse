# 🚀 Auto Task Reminder API

A lightweight **FastAPI-based backend system** that allows users to create tasks and automatically receive reminders using background job scheduling.

This project demonstrates **real-world backend concepts** such as:

* API design with FastAPI
* Database integration with SQLAlchemy
* Background task automation using APScheduler

---

## ✨ Features

* ✅ Create tasks with a due time
* 📋 View all tasks
* ✔️ Mark tasks as completed
* ⏰ Automatic reminder system (background scheduler)
* 🔔 Prevents duplicate notifications

---

## 🏗️ Tech Stack

* **FastAPI** – API framework
* **SQLite** – Lightweight database
* **SQLAlchemy** – ORM
* **APScheduler** – Background job scheduler

---

## 📂 Project Structure

```
├──TaskPulse/
  ├──app/
  ├── models.py        # SQLAlchemy models
  ├── schemas.py       # Pydantic schemas
  ├── routes.py        # API routes
├── database.py      # Database setup
├── main.py          # App entry point
├── scheduler.py     # Background job logic
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/task-reminder-api.git
cd task-reminder-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
uvicorn app.main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

### Create Task

```json
{
  "title": "Study FastAPI",
  "description": "Finish project",
  "due_time": "2026-03-26T14:00:00"
}
```

---

## 🤖 How Automation Works

1. Tasks are stored in the database
2. Background scheduler runs every minute
3. It checks for tasks that are due
4. Prints a reminder in the console
5. Marks task as notified

---

## 📌 Future Improvements

* 📧 Email notifications
* 🔐 User authentication
* 📊 Task filtering & pagination
* 🌍 Deployment (Docker, cloud)

---

## 🧠 Learning Value

This project showcases:

* Backend architecture design
* Background processing
* Clean API structure
* Real-world automation logic

---

## 📜 License

This project is open-source and available under the MIT License.
