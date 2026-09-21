expenses = []


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\nRecorded Expenses:")

        for i, expense in enumerate(expenses, 1):
            print(i, expense["category"], ":", expense["amount"])


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses:", total)


def highest_expense():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        highest = max(expenses, key=lambda x: x["amount"])

        print("Highest Expense:")
        print("Category:", highest["category"])
        print("Amount:", highest["amount"])


def expenses_by_category():
    category = input("Enter category: ")
    found = False

    print("\nExpenses in", category, ":")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print(expense["amount"])
            found = True

    if not found:
        print("No expense found in this category.")


while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Find Highest Expense")
    print("5. Display Expenses by Category")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        highest_expense()

    elif choice == "5":
        expenses_by_category()

    elif choice == "6":
        print("Expense Tracker closed!")
        break

    else:
        print("Invalid choice! Try again.")

# concept: List expenses store karti hai → Dictionary category + amount rakhti hai → Functions Add/View/Total/Highest/Category operations perform karte hain → while loop program ko running rakhta hai        