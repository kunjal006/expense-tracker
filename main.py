expenses = []

while True:
    print("\n-------Expense Tracker-----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("Add expense selected")
    elif choice == "2" : 
        print("View expense selected")
    elif choice == "3":
        break
    else:
        print("Invalid choice")