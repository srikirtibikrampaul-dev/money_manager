# ==========================================
#          MONEY MANAGER
#     Personal Finance Tracker
# ==========================================

# Lists to store income and expenses
income_list = []
expense_list = []

# Categories for expenses
categories = [
    "Food",
    "Transport",
    "Shopping",
    "Education",
    "Entertainment",
    "Bills",
    "Other"
]


# Function to add income
def add_income():
    amount = float(input("Enter income amount: ₹"))
    
    if amount <= 0:
        print("Please enter a valid amount.")
        return

    income_list.append(amount)
    print("Income added successfully!")


# Function to add expense
def add_expense():
    amount = float(input("Enter expense amount: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
        return

    print("\nExpense Categories:")

    for i in range(len(categories)):
        print(i + 1, ".", categories[i])

    choice = int(input("Select category: "))

    if choice < 1 or choice > len(categories):
        print("Invalid category.")
        return

    category = categories[choice - 1]

    expense = {
        "amount": amount,
        "category": category
    }

    expense_list.append(expense)

    print("Expense added successfully!")


# Function to calculate total income
def total_income():
    return sum(income_list)


# Function to calculate total expenses
def total_expense():
    total = 0

    for expense in expense_list:
        total += expense["amount"]

    return total


# Function to show category-wise expenses
def category_summary():
    print("\n========== CATEGORY SUMMARY ==========")

    for category in categories:
        total = 0

        for expense in expense_list:
            if expense["category"] == category:
                total += expense["amount"]

        if total > 0:
            print(category, ": ₹", total)


# Function to find highest expense
def highest_expense():
    if len(expense_list) == 0:
        print("No expenses recorded yet.")
        return

    highest = expense_list[0]

    for expense in expense_list:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n========== HIGHEST EXPENSE ==========")
    print("Category :", highest["category"])
    print("Amount   : ₹", highest["amount"])


# Function to display all expenses
def show_expenses():
    if len(expense_list) == 0:
        print("No expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    for i, expense in enumerate(expense_list):
        print(
            i + 1,
            ".",
            expense["category"],
            "- ₹",
            expense["amount"]
        )


# Function to display complete summary
def financial_summary():
    income = total_income()
    spending = total_expense()
    balance = income - spending

    print("\n====================================")
    print("       FINANCIAL SUMMARY")
    print("====================================")
    print("Total Income   : ₹", income)
    print("Total Spending : ₹", spending)
    print("Remaining      : ₹", balance)
    print("Transactions   :", len(expense_list))

    if balance > 0:
        print("Status         : You are within your income.")
    elif balance == 0:
        print("Status         : Income and spending are equal.")
    else:
        print("Status         : You have exceeded your income.")


# Main program
while True:

    print("\n")
    print("====================================")
    print("          💰 MONEY MANAGER")
    print("====================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Total Income")
    print("4. Show Total Spending")
    print("5. Show Remaining Balance")
    print("6. Show Category Summary")
    print("7. Show Highest Expense")
    print("8. Show All Expenses")
    print("9. Financial Summary")
    print("10. Exit")
    print("====================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        print("\nTotal Income: ₹", total_income())

    elif choice == "4":
        print("\nTotal Spending: ₹", total_expense())

    elif choice == "5":
        balance = total_income() - total_expense()
        print("\nRemaining Balance: ₹", balance)

    elif choice == "6":
        category_summary()

    elif choice == "7":
        highest_expense()

    elif choice == "8":
        show_expenses()

    elif choice == "9":
        financial_summary()

    elif choice == "10":
        print("\nThank you for using Money Manager!")
        break

    else:
        print("Invalid choice. Please try again.")