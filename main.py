expenses = []

while True:
    print("\n-------Expense Tracker-----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        amnt = int(input("Enter the amount: "))
        expense_id = len(expenses) + 1
        expense = {
            "id": expense_id,
            "title": title,
            "amount": amnt
        }
        expenses.append(expense)
        print("Expenses added successfully")
    elif choice == "2" : 
        if not expenses:
            print("No expenses found")
        else:
            for expense in expenses:
                print("ID :", expense["id"],
                    "| Title: ", expense["title"],
                    "| Amount:", expense["amount"]
                )
    elif choice == "3":
        break
    else:
        print("Invalid choice")