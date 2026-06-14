expenses = []
next_id = 1

while True:
    print("\n-------Expense Tracker-----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        amnt = int(input("Enter the amount: "))
        expense = {
            "id": next_id,
            "title": title,
            "amount": amnt
        }
        expenses.append(expense)
        next_id += 1
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
        id_del = int(input("Enter the id you want to delete: "))
        found = False
        for expense in expenses:
            if id_del == expense["id"]:
                expenses.remove(expense)
                found = True
                print("Expense deleted successfully")
                break
        if not found:
            print("Expense not found")
    elif choice == "4":
        break
    else:
        print("Invalid choice")