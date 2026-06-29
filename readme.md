# 💰 Expense Tracker

A version-by-version backend development project built to learn **Python**, **PostgreSQL**, **FastAPI**, and modern REST API development from scratch.

Instead of building everything at once, this project evolves with every version, introducing new backend concepts step-by-step while following industry practices.

---

# 🗺️ Project Roadmap

| Version | Description                                    
| ------- | ---------------------------------------------- 
| ✅ V1    | Pure Python CRUD (In-Memory)                   
| ✅ V2    | OOP Refactor + Categories + Monthly Summary    
| ✅ V3    | JSON Persistence + Search + Filter + Analytics 
| ✅ V4    | PostgreSQL + FastAPI REST API                  
| ✅ V5   | JWT Authentication + User Accounts             

---

# ✨ Features

### Expense Management

* ✅ Add Expense
* ✅ View All Expenses
* ✅ Update Expense
* ✅ Delete Expense

### Search & Filtering

* ✅ Search expenses by title
* ✅ Filter expenses by category
* ✅ Category-wise summary
* ✅ Expense analytics

### Data Management

* ✅ PostgreSQL persistent storage
* ✅ CSV export
* ✅ JSON persistence (V3)
* ✅ Monthly expense summary
* ✅ Highest & Lowest expense finder

### API Features

* ✅ RESTful API
* ✅ FastAPI
* ✅ Swagger UI Documentation
* ✅ Pydantic Validation
* ✅ Proper HTTP Status Codes
* ✅ HTTP Exception Handling

---

# 🛠 Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| FastAPI      | Backend Framework    |
| PostgreSQL   | Database             |
| psycopg2     | PostgreSQL Driver    |
| Pydantic     | Data Validation      |
| Swagger UI   | API Documentation    |
| Git & GitHub | Version Control      |

---

# 📁 Project Structure

```text
expense_tracker/
│
├── app.py              
├── database.py         
├── main.py             
├── expenses.csv        
├── expenses.json       
├── README.md
├── .gitignore
│
└── __pycache__/        
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/expense_tracker.git
cd expense_tracker
```

---

## 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn psycopg2-binary
```

---

## 3️⃣ Setup PostgreSQL

Create Database

```sql
CREATE DATABASE expense_tracker;
```

Create Table

```sql
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    amount INTEGER NOT NULL,
    category VARCHAR(50) NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 4️⃣ Run the Server

```bash
python -m uvicorn app:app --reload
```

---

## 5️⃣ Open Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoints

| Method | Endpoint                       | Description                 |
| ------ | ------------------------------ | --------------------------- |
| GET    | `/expenses`                    | Get all expenses            |
| POST   | `/expenses`                    | Create a new expense        |
| PUT    | `/expenses/{id}`               | Update an existing expense  |
| DELETE | `/expenses/{id}`               | Delete an expense           |
| GET    | `/expenses/search?title=`      | Search expenses by title    |
| GET    | `/expenses/category?category=` | Filter expenses by category |
| GET    | `/expenses/summary`            | Expense summary by category |

---

# 🔐 Authentication & User Management (V5)



### Planned Features

* ✅ User Registration
* ✅ Secure Password Hashing (bcrypt)
* ✅ User Login
* ✅ JWT Authentication
* ✅ Access Tokens
* ✅ Protected Routes
* ✅ OAuth2PasswordBearer
* ✅ Multi-user Expense Tracking
* ✅ Each user can access only their own expenses

---

# 📚 Concepts Learned

* Python
* Object-Oriented Programming
* File Handling
* JSON
* CSV
* SQL
* PostgreSQL
* CRUD Operations
* REST APIs
* FastAPI
* Pydantic
* HTTP Status Codes
* Exception Handling
* Git & GitHub


---

# 🎯 Project Goal

This project is part of my backend development journey and is being built version-by-version to gain a strong understanding of backend engineering, databases, REST APIs, authentication, and modern Python development.

Each version introduces new concepts while improving the architecture of the previous one.

---

## ⭐ If you found this project useful, consider giving it a star!
