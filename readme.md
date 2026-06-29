# 💰 Expense Tracker

A backend application built version-by-version using Python, PostgreSQL, and FastAPI.

## 🗺️ Versions

| Version | Description | Status |
|---------|-------------|--------|
| V1 | Pure Python CRUD (in-memory) | 
| V2 | OOP Refactor + Categories + Monthly Summary | 
| V3 | JSON Persistence + Search + Filter + Analytics | 
| V4 | PostgreSQL + FastAPI REST API |  
| V5 | JWT Authentication + User Accounts |

## ✨ Features

- Add, View, Update, Delete expenses
- Category-wise filtering
- Search by title
- Monthly summary with percentage breakdown
- Highest & Lowest expense finder
- Auto CSV export on every change
- PostgreSQL persistent storage
- REST API with FastAPI

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** psycopg2
- **API Docs:** Swagger UI (auto-generated)
- **Auth (V5):** JWT

## 📁 Project Structure
expense_tracker/
├── app.py # FastAPI routes
├── database.py # PostgreSQL connection
├── main.py # CLI version (V1-V3)
├── expenses.csv # Auto-exported CSV
└── README.md


## 🚀 How to Run

### 1. Setup PostgreSQL
```bash
psql -U postgres
CREATE DATABASE expense_tracker;
\c expense_tracker
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    amount INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Install Dependencies
```bash
pip install fastapi uvicorn psycopg2-binary
```

### 3. Run the API
```bash
python -m uvicorn app:app --reload
```

### 4. Open API Docs
http://127.0.0.1:8000/docs


## 📡 API Endpoints (V4)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/expenses` | Get all expenses |
| POST | `/expenses` | Add new expense |
| PUT | `/expenses/{id}` | Update expense |
| DELETE | `/expenses/{id}` | Delete expense |

## 🔐 Authentication (V5)

- User Registration
- Login with JWT tokens
- Personal expense tracking per user