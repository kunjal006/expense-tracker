import json


class ExpenseTracker:
    def __init__(self):
        self.categories = [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Other"
        ]
        self.load_expenses()
    

    def load_expenses(self):
        try:
            with open("expenses.json","r") as file:
                data = json.load(file)

            self.expenses = data

            if self.expenses:
                last_id = self.expenses[-1]["id"]
                self.next_id = last_id + 1
            else:
                self.next_id = 1
        except FileNotFoundError:
            self.expenses = []
            self.next_id = 1


    def save_expenses(self):
        with open("expenses.json","w") as file:
            json.dump(self.expenses,file, indent=4)

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
        if not self.expenses:
            print("No expenses found")
        else:
            for expense in self.expenses:
                print(
                    "ID :", expense["id"],
                    "| Title:", expense["title"],
                    "| Amount:", expense["amount"],
                    "| Category:", expense["category"]
                )
    
    def add_expense(self):
        title = input("Enter the title: ")
        amnt = self.get_valid_number("Enter the amount: ")
        category = self.get_category()
        expense = {
            "id": self.next_id,
            "title": title,
            "amount": amnt,
            "category": category
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expenses added successfully")
        self.next_id += 1

    def delete_expense(self):
        id_del = self.get_valid_number("Enter the id you want to delete: ")
        found = False
        for expense in self.expenses:
            if id_del == expense["id"]:
                self.expenses.remove(expense)
                self.save_expenses()
                found = True
                print("Expense deleted successfully")
                break
        if not found:
            print("Expense not found")

    def update_expense(self):
        if not self.expenses:
                print("No expenses found")
        else:
            id_upd = self.get_valid_number("Enter the id you want to update: ")
            found = False
            for expense in self.expenses:
                if id_upd == expense["id"]:
                    print("What do you want to update?")
                    print("1. Title")
                    print("2. Amount")
                    print("3. Category")
                    op = input("Enter your choice: ")
                    if op == "1":
                        title = input("Enter the title: ")
                        expense["title"] = title
                        print("Name changed successfully")
                    elif op == "2":
                        amount = self.get_valid_number("Enter your amount: ")
                        expense["amount"] = amount
                        print("Amount changed successfully")
                    elif op == "3":
                    
                        expense["category"] = self.get_category()
                        print("Category changed successfully")

                    else:
                        print("Invalid choice")
                    self.save_expenses()
                    found = True
                    break
            if not found:
                print("Expense not found")
    
    def monthly_summary(self):
        total = 0
        summary = {
            "Food":0,
            "Travel":0,
            "Shopping":0,
            "Bills":0,
            "Other":0
        }
        if not self.expenses:
            print("No expenses found")
            return
        for expense in self.expenses:
            amount = expense["amount"]
            category = expense["category"]

            total += amount
            summary[category] += amount
        print("----Monthly expenses---")
        print("Total expenses", total)
        for category,amount in summary.items():
            print(category, ":", amount)

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
        found = False
        for expense in self.expenses:
            if expense["category"] == selectedCategory:
                found = True
                print(
                    "ID :", expense["id"],
                    "| Title:", expense["title"],
                    "| Amount:", expense["amount"],
                    "| Category:", expense["category"]
                )
        if not found:
            print("No expense found")
    
    def search_by_name(self):
        search = input("Enter name: ")
        search = search.lower()
        
        found = False

        for expense in self.expenses:
            title = expense["title"].lower()

            if search in title:
                print(
                    "ID :", expense["id"],
                    "| Title:", expense["title"],
                    "| Amount:", expense["amount"],
                    "| Category:", expense["category"]
                )
        if not found:
            print("No expense found")


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
    print("8. Exit")


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
        break
    else:
        print("Invalid choice")