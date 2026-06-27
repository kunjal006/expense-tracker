from database import get_connection


class ExpenseTracker:
    def __init__(self):
        self.categories = [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Other"
        ]
 

    def get_valid_number(self, message):
        while True:
            try:
                number = int(input(message))
                if number > 0:
                    return number
                else:
                    print("Number must be greater than 0")
            except ValueError:
                print("Please enter a valid number")

    def view_expense(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM expenses
            """
        )
        expenses = cursor.fetchall()
        if not expenses:
            print("No expenses found")
        else:
            for expense in expenses:
                print(
                    "ID :", expense[0],
                    "| Title:", expense[1],
                    "| Amount:", expense[2],
                    "| Category:", expense[3],
                    "| Date:", expense[4]
                )
        cursor.close()
        conn.close()
    
    def add_expense(self):
        title = input("Enter the title: ")
        amnt = self.get_valid_number("Enter the amount: ")
        category = self.get_category()
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO expenses (title, amount, category)
            VALUES (%s, %s, %s)
            """,
            (title, amnt, category)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Expenses added successfully")

    def delete_expense(self):
        id_del = self.get_valid_number("Enter the id you want to delete: ")
        conn =get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            DELETE FROM expenses WHERE id = %s
            """,
            (id_del,)
        )
        if cursor.rowcount > 0:
            print("Expense deleted Successfully")
            conn.commit()
        else:
            print("Expense not found")
        
        cursor.close()
        conn.close()

    def update_expense(self):
            id_upd = self.get_valid_number("Enter the id you want to update: ")
            conn = get_connection()
            cursor = conn.cursor()
            print("What do you want to update?")
            print("1. Title")
            print("2. Amount")
            print("3. Category")
            op = input("Enter your choice: ")
            if op == "1":
                title = input("Enter the title: ")
                cursor.execute(
                    """
                    UPDATE expenses
                    SET title = %s
                    WHERE id = %s;
                    """,
                    (title, id_upd)
                    )
                if cursor.rowcount > 0:
                    conn.commit()
                    print("Name changed Successfully")
                else:
                    print("Expense not found")
            elif op == "2":
                amount = self.get_valid_number("Enter your amount: ")
                cursor.execute(
                    """
                    UPDATE expenses
                    SET amount = %s
                    WHERE id = %s;
                    """,
                    (amount, id_upd)
                    )
                if cursor.rowcount > 0:
                    conn.commit()
                    print("Amount changed Successfully")
                else:
                    print("Expense not found")
            elif op == "3":
                cat = self.get_category()
                cursor.execute(
                    """
                    UPDATE expenses
                    SET category = %s
                    WHERE id = %s;
                    """,
                    (cat, id_upd)
                    )
                if cursor.rowcount > 0:
                    conn.commit()
                    print("Category changed Successfully")
                else:
                    print("Expense not found")
            
            else:
                print("Invalid choice")
            cursor.close()
            conn.close()
    
    def monthly_summary(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT category, SUM(amount)
            FROM expenses
            GROUP BY category;"""
        )
        expenses = cursor.fetchall()

        if not expenses:
            print("No expenses found")
            cursor.close()
            conn.close()
            return
        
        total = 0

        for expense in expenses:
            total += expense[1]

        print("----Monthly expenses---")
        print("Total expenses", total)
        for expense in expenses:
            category = expense[0]
            amount = expense[1]
            percentage = (amount / total) * 100

            print(f"{category}: ₹{amount} ({percentage:.2f}%)")

        cursor.close()
        conn.close()

    def get_category(self):
        print("Choose Category: ")
        for i, category in enumerate(self.categories, start=1):
            print(i, ".", category)
        while True:
            category_choice = self.get_valid_number("Enter category number: ")

            if 1 <= category_choice <= len(self.categories):
                category = self.categories[category_choice -1]
                return category
            else:
                print("Invalid Choice")

    def filter_by_Category(self):
        selectedCategory = self.get_category()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM expenses
            WHERE category = %s;
            """,
            (selectedCategory,)
        )
        expenses = cursor.fetchall()
        if not expenses:
            print("No expenses found")
        else:
            for expense in expenses:
                print(
                    "ID :", expense[0],
                    "| Title:", expense[1],
                    "| Amount:", expense[2],
                    "| Category:", expense[3],
                    "| Date:", expense[4]
                )
        cursor.close()
        conn.close()

    def search_by_name(self):
        search = input("Enter name: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
        """
        SELECT * FROM expenses
        WHERE LOWER(title) LIKE LOWER(%s);
        """,
        (f"%{search}%",))
        expenses = cursor.fetchall()

        if not expenses:
            print("No expense found")
        else:
            for expense in expenses:
                print(
                "ID :", expense[0],
                "| Title:", expense[1],
                "| Amount:", expense[2],
                "| Category:", expense[3],
                "| Date:", expense[4]
                )
        cursor.close()
        conn.close()
        
    def highest_expense(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM expenses
            ORDER BY amount DESC
            LIMIT 1;
            """
        )
        expense = cursor.fetchone()
        if not expense:
            print("No expenses found")
            return
        else:
            print(
                    "ID :", expense[0],
                    "| Title:", expense[1],
                    "| Amount:", expense[2],
                    "| Category:", expense[3],
                    "| Date:", expense[4]
                )
        cursor.close()
        conn.close()

    def lowest_expense(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT *
            FROM expenses
            ORDER BY amount ASC
            LIMIT 1;
            """
        )
        expense = cursor.fetchone()
        if not expense:
            print("No expenses found")
            return
        else:
            print(
                    "ID :", expense[0],
                    "| Title:", expense[1],
                    "| Amount:", expense[2],
                    "| Category:", expense[3],
                    "| Date:", expense[4]
                )
        cursor.close()
        conn.close()



tracker = ExpenseTracker()


def display_menu():
    print("\n-------Expense Tracker-----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. Update expense")
    print("5. Monthly summary")
    print("6. Filter by Category")
    print("7. Search by Title Name")
    print("8. Highest expense")
    print("9. Lowest expense")
    print("10. Exit")


while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
       tracker.add_expense()
    elif choice == "2" : 
        tracker.view_expense()
    elif choice == "3":
        tracker.delete_expense()
    elif choice == "4":
        tracker.update_expense()
    elif choice == "5":
        tracker.monthly_summary()
    elif choice == "6":
        tracker.filter_by_Category()
    elif choice == "7":
        tracker.search_by_name()
    elif choice == "8":
        tracker.highest_expense()
    elif choice == "9":
        tracker.lowest_expense()
    elif choice == "10":
        break
    else:
        print("Invalid choice")