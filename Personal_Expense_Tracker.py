# Simple input and storage in a key-value pair (dictionary)

import csv
import os
import datetime

CSV_FILE = 'expenses.csv'


def save_expense_to_csv(expense_details, filename=CSV_FILE):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(expense_details)


def load_expenses_from_csv(filename=CSV_FILE):
    expenses = []
    if not os.path.isfile(filename):
        return expenses
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['amount'] = float(row['amount'])
            expenses.append(row)
    return expenses


# List to store all expenses
def add_expense(expenses):
    while True:
        expense_date = input("Enter the expense date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(expense_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Error: Please enter the date in YYYY-MM-DD format.")

    category = input("Enter the expense category: ")
    while True:
        amount = input("Enter the amount spent: ")
        try:
            amount = float(amount)
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid amount.")

    description = input("Enter a brief description: ")

    expense_details = {
        "date": expense_date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(expense_details)
    save_expense_to_csv(expense_details)
    print("Expense added. Now total expenses are:", expenses)


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nAll Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(
            f"{idx}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        
def track_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    month = input("Enter the month to track (YYYY-MM): ")
    budget = 10000  # Fixed monthly budget
    print(f"Monthly budget is set to: {budget}")
    # Calculate total expenses for the month
    total = 0
    for expense in expenses:
        if expense['date'].startswith(month):
            total += float(expense['amount'])
    print(f"\nTotal expenses for {month}: {total}")
    if total > budget:
        print(f"Warning: You have exceeded your budget by {total - budget}!")
    else:
        print(f"You are within your budget. Remaining balance: {budget - total}")


def save_all_expenses(expenses):
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Only write header if file is empty
        if os.stat(CSV_FILE).st_size == 0:
            writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
    print(f"All current expenses appended to {CSV_FILE}.")


def menu():
    expenses = load_expenses_from_csv()
    while True:
        print("\nPersonal Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Monthly Budget")
        print("4. Save All Expenses to CSV")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            track_expenses(expenses)
        elif choice == '4':
            save_all_expenses(expenses)
        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


# Add 5 random expenses for Jan 2025 to exceed the budget


if __name__ == "__main__":
    menu()




