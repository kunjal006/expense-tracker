# 💰 Expense Tracker

A terminal-based expense tracking application built with Python and PostgreSQL.

## Versions
- ✅ V1 - Pure Python CRUD (in-memory storage)
- ✅ V2 - OOP Refactor + Categories + Monthly Summary
- ✅ V3 - JSON Persistence + Search + Filter + Analytics
- ✅ V4 - PostgreSQL Integration (current)

## Features
- Add, View, Update, Delete expenses
- Category-wise filtering
- Search by title
- Monthly summary with percentage breakdown
- Highest & Lowest expense finder
- Persistent storage with PostgreSQL

## Tech Stack
Python, OOP, JSON, PostgreSQL, psycopg2

## How to Run
1. Setup PostgreSQL and create database
```bash
psql -U postgres
CREATE DATABASE expense_tracker;
```
2. Update database credentials in `database.py`
3. Run the app
```bash
python main.py
```