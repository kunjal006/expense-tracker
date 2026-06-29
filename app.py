from fastapi import FastAPI, HTTPException
from database import get_connection
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

class Category(str, Enum):
    Food = "Food"
    Travel = "Travel"
    Shopping = "Shopping"
    Bills = "Bills"
    Other = "Other"

class Expense(BaseModel):
    title: str
    amount: int = Field(gt=0)
    category: Category


@app.get("/")
def home():
    return {
        "message":"Expense tracker API is running!"
    }

@app.get("/expenses")
def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT * FROM expenses
                   ORDER BY id ASC
                   """)
    expenses = cursor.fetchall()

    expense_list = []

    for expense in expenses:
        expense_data = {
            "id": expense[0],
            "title": expense[1],
            "amount": expense[2],
            "category": expense[3],
            "date": expense[4]
        }

        expense_list.append(expense_data)

    cursor.close()
    conn.close()

    return expense_list

@app.post("/ expenses")
def add_expenses(expense: Expense):
    conn= get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses (title, amount, category)
        VALUES (%s, %s, %s)""",
        (
            expense.title,
            expense.amount,
            expense.category
        )
    )

    conn.commit()

    cursor.close()
    conn.commit()

    return {"message": "Expense added successfully"}

@app.put("/expenses/{id}")
def update_expense(id: int, expense: Expense):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses SET
        title = %s,
        amount = %s,
        category = %s
        WHERE id = %s """, 
        (
            expense.title,
            expense.amount,
            expense.category,
            id
        )

    )
    try:
        if cursor.rowcount > 0:
            conn.commit()
            return {"message": "Changes made successfully"}
        else:
            raise HTTPException(
            status_code=404,
            detail="Expense not found"
            )
    finally:
        cursor.close()
        conn.close()

@app.delete("/expenses/{id}")
def delete_expenses(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM expenses WHERE id = %s
        """,
        (id,)
    )
    try:
        if cursor.rowcount > 0:
            conn.commit()
            return {"message": "Deleted Successfully"}
        else:
            raise HTTPException(
        status_code=404,
        detail="Expense not found"
)
    finally:
        cursor.close()
        conn.close()

@app.get("/expenses/search")
def search_expense(title:str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM expenses
        WHERE LOWER(title) LIKE LOWER(%s);""",
        (f"%{title}%",)
    )

    expenses = cursor.fetchall()

    result = []

    for expense in expenses:
        expense_data = {
            "id": expense[0],
            "title": expense[1],
            "amount": expense[2],
            "category": expense[3],
            "date": expense[4]
        }
        result.append(expense_data)
    cursor.close()
    conn.close()

    return result

@app.get("/expenses/category")
def filter_category(category: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT *
                    FROM expenses
                    WHERE LOWER(category) = LOWER(%s);""",
                    (category,))
    
    expenses = cursor.fetchall()

    result = []

    for expense in expenses:
        expense_data = {
            "id": expense[0],
            "title": expense[1],
            "amount": expense[2],
            "category": expense[3],
            "date": expense[4]
        }
        result.append(expense_data)
    cursor.close()
    conn.close()
    return result

@app.get("/expenses/summary")
def get_summary():
    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT category,
            SUM(amount)
            FROM expenses
            GROUP BY category;"""
        )

        category_summary = cursor.fetchall()

        cursor.execute(
            """
            SELECT SUM(amount)
            FROM expenses;"""
        )

        total = cursor.fetchone()
        grand_total = total[0] if total[0] else 0

        expense_list = []

        for expense in category_summary:
            percentage = (
                (expense[1] / grand_total) * 100
                if grand_total > 0
                else 0
            )

            expense_data = {
                "category": expense[0],
                "amount": expense[1],
                "percentage": round(percentage, 2)
            }
            expense_list.append(expense_data)

        return {
            "total": grand_total,
            "categories": expense_list
        }
    finally:
        cursor.close()
        conn.close()