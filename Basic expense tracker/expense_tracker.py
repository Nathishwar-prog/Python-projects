import json
import os
from datetime import datetime

# File to store expenses
EXPENSES_FILE = "expenses.json"


def load_expenses():
    """Load expenses from the JSON file."""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    """Add a new expense."""
    amount = float(input("Enter amount spent: "))
    category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip().title()
    description = input("Enter a brief description (optional): ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses():
    """View all expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpense History:")
    print("-" * 50)
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. Amount: ${expense['amount']:.2f}")
        print(f"   Category: {expense['category']}")
        print(f"   Description: {expense['description']}")
        print(f"   Date: {expense['date']}")
        print("-" * 50)


def expense_summary():
    """Show summary of expenses by category."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    total = 0

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount
        total += amount

    print("\nExpense Summary:")
    print("-" * 30)
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")
    print("-" * 30)
    print(f"Total Expenses: ${total:.2f}")
    print("-" * 30)


def main():
    """Main function to run the expense tracker."""
    global expenses
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expense Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()