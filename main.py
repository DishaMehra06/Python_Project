import csv

# Global list to store expenses
expenses = []

# Load expenses from file
def load_expenses(filename="expenses.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print("No existing expense file found. Starting fresh!")

# Save expenses to file
def save_expenses(filename="expenses.csv"):
    with open(filename, "w", newline="") as file:
        fieldnames = ["amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# Add a new expense
def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    description = input("Enter a short description: ")
    expenses.append({"amount": amount, "category": category, "description": description})
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Expenses ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['amount']} - {expense['category']} - {expense['description']}")
    print("\n")

# Delete an expense
def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            deleted = expenses.pop(index)
            print(f"Deleted expense: {deleted}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Invalid input!")

# Main menu
def main():
    load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit and Save")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            save_expenses()
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
