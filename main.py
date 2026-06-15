expenses = []
next_id = 1


def display_menu():
    print("\n-------Expense Tracker-----")
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete expense")
    print("4. Update expense")
    print("5. Exit")

def add_expense(expenses,next_id):
    title = input("Enter the title: ")
    amnt = int(input("Enter the amount: "))
    expense = {
        "id": next_id,
        "title": title,
        "amount": amnt
    }
    expenses.append(expense)
    print("Expenses added successfully")
    return next_id + 1

def view_expense(expenses):
    if not expenses:
            print("No expenses found")
    else:
        for expense in expenses:
            print("ID :", expense["id"],
                "| Title: ", expense["title"],
                "| Amount:", expense["amount"]
            )

def delete_expense(expenses):
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

def update_expense(expenses):
    if not expenses:
            print("No expenses found")
    else:
        id_upd = int(input("Enter the id you want to update: "))
        found = False
        for expense in expenses:
            if id_upd == expense["id"]:
                print("What do you want to update?")
                print("1. Title")
                print("2. Amount")
                op = input("Enter your choice: ")
                if op == "1":
                    title = input("Enter the title: ")
                    expense["title"] = title
                    print("Name changed successfully")
                elif op == "2":
                    amount = int(input("Enter your amount: "))
                    expense["amount"] = amount
                    print("Amount changed successfully")
                else:
                    print("Invalid choice")
                found = True
                break
        if not found:
            print("Expense not found")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
       next_id = add_expense(expenses,next_id)
    elif choice == "2" : 
        view_expense(expenses)
    elif choice == "3":
        delete_expense(expenses)
    elif choice == "4":
        update_expense(expenses)
    elif choice == "5":
        break
    else:
        print("Invalid choice")