
import json

expenses = []


def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (DD-MM-YYYY): ")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }

        expenses.append(expense)
        save_expenses()

        print("✅ Expense added successfully!")

    except:
        print("❌ Invalid input. Please try again.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']}")


def show_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total spending: ${total}")


def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter expense number to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses()
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except:
        print("Error deleting expense.")


def show_menu():
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")

load_expenses()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
        