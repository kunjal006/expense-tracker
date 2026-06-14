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
        print(expenses)
    elif choice == "2" : 
        print("View expense selected")
    elif choice == "3":
        break
    else:
        print("Invalid choice")