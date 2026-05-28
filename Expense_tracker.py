expenses = []

# ---------------- FUNCTIONS ---------------- #

def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = float(input("Enter Amount ₹: "))

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
   

    print(" Expense Added Successfully!")


def view_expenses():
    print("\n--- All Expenses $$ ---")

    if not expenses:
        print("⚠️ No Expenses Found")
        return

    print("DATE | CATEGORY | DESCRIPTION | AMOUNT")
    print("-" * 45)

    for i, expense in enumerate(expenses, start=1):

         print(
            f"{i}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"₹{expense['amount']}"
        )

def total_spending():
    total = sum(i["amount"] for i in expenses)

    print(f"\n Total Spending: ₹{total}")


def category_wise_spending():
    print("\n--- Category Wise Spending ---")

    if not expenses:
        print("No Expenses Found")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]

        summary[category] = summary.get(category, 0) + expense["amount"]

    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")


# ---------------- MAIN PROGRAM ---------------- #

print(" Welcome To Expense Tracker ")

while True:

    print("\n========= MENU =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Category Wise Spending")
    print("5. Exit")
    print("========================")

    choice = input("Enter Choice (1-5): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        category_wise_spending()

    elif choice == "5":
        print("\n Thank You For Using Expense Tracker")
        break

    else:
        print(" Invalid Choice")