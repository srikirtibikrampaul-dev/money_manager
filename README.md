# 💰 Money Manager

### A Simple Python-Based Personal Finance & Expense Tracking System

**Money Manager** is a beginner-friendly personal finance management application developed using **Python**. It allows users to record their income and expenses, categorize spending, monitor their balance, and generate a basic financial summary.

The project was developed as part of the **Python Essentials** flipped course evaluation and demonstrates fundamental Python programming concepts through a practical real-world application.

---

## 📌 Project Overview

Managing personal finances can become difficult when income and expenses are not properly tracked. Money Manager provides a simple command-line solution that helps users keep track of their financial activity.

The application allows users to:

* Add income
* Record expenses
* Categorize expenses
* Calculate total income
* Calculate total spending
* Calculate remaining balance
* View category-wise spending
* Identify the highest expense
* View all recorded expenses
* Generate a complete financial summary

The project focuses on applying Python fundamentals to solve a practical problem.

---

## ✨ Features

### 💵 1. Add Income

Users can enter their income amount and add it to their financial records.

Example:

```text
Enter income amount: ₹20000

Income added successfully!
```

---

### 💸 2. Add Expenses

Users can record their expenses by entering the amount and selecting an appropriate category.

Available categories include:

* Food
* Transport
* Shopping
* Education
* Entertainment
* Bills
* Other

Example:

```text
Enter expense amount: ₹1500

Expense Categories:
1. Food
2. Transport
3. Shopping
4. Education
5. Entertainment
6. Bills
7. Other

Select category: 1

Expense added successfully!
```

---

### 📊 3. Total Income

The application calculates the total amount of income entered by the user.

```text
Total Income: ₹20000
```

---

### 📉 4. Total Spending

The application automatically calculates the total amount spent across all expense transactions.

```text
Total Spending: ₹6500
```

---

### 💰 5. Remaining Balance

The remaining balance is calculated using:

```text
Remaining Balance = Total Income - Total Spending
```

Example:

```text
Total Income   : ₹20000
Total Spending : ₹6500
Remaining      : ₹13500
```

---

### 🗂️ 6. Category-Wise Expense Summary

The program groups expenses according to their category.

Example:

```text
========== CATEGORY SUMMARY ==========

Food          : ₹2500
Transport     : ₹1200
Shopping      : ₹1800
Entertainment : ₹1000
```

This helps users understand where most of their money is being spent.

---

### 🔝 7. Highest Expense

The program identifies the largest individual expense.

Example:

```text
========== HIGHEST EXPENSE ==========

Category : Shopping
Amount   : ₹1800
```

---

### 📋 8. View All Expenses

Users can view all recorded expenses along with their categories.

Example:

```text
========== ALL EXPENSES ==========

1. Food - ₹500
2. Transport - ₹200
3. Shopping - ₹1800
4. Food - ₹750
```

---

### 📑 9. Financial Summary

The financial summary provides an overview of the user's current financial situation.

Example:

```text
====================================
       FINANCIAL SUMMARY
====================================
Total Income   : ₹20000
Total Spending : ₹6500
Remaining      : ₹13500
Transactions   : 4
Status         : You are within your income.
```

---

## 🖥️ Main Menu

The application provides a simple menu-driven interface:

```text
====================================
          💰 MONEY MANAGER
====================================
1. Add Income
2. Add Expense
3. Show Total Income
4. Show Total Spending
5. Show Remaining Balance
6. Show Category Summary
7. Show Highest Expense
8. Show All Expenses
9. Financial Summary
10. Exit
====================================
```

---

## 🛠️ Technologies Used

| Technology             | Purpose                          |
| ---------------------- | -------------------------------- |
| Python                 | Core programming language        |
| Lists                  | Storing income and expenses      |
| Dictionaries           | Storing expense details          |
| Functions              | Organizing program functionality |
| Loops                  | Processing transactions          |
| Conditional Statements | Decision making                  |
| `sum()`                | Calculating totals               |
| User Input             | Collecting financial information |

---

## 🧠 Python Concepts Demonstrated

This project demonstrates several fundamental Python concepts.

### 1. Variables

Variables are used to store values such as income, expenses, categories, and user choices.

```python
amount = float(input("Enter income amount: ₹"))
```

### 2. Lists

Lists are used to store multiple income and expense records.

```python
income_list = []
expense_list = []
```

### 3. Dictionaries

Dictionaries are used to store information about individual expenses.

```python
expense = {
    "amount": amount,
    "category": category
}
```

### 4. Functions

Functions divide the program into smaller and reusable components.

Examples:

```python
add_income()
add_expense()
total_income()
total_expense()
category_summary()
highest_expense()
financial_summary()
```

### 5. Loops

Loops are used to process multiple transactions and display categories.

```python
for expense in expense_list:
    total += expense["amount"]
```

### 6. Conditional Statements

Conditional statements are used for validation and decision-making.

```python
if amount <= 0:
    print("Please enter a valid amount.")
```

### 7. User Input

The program interacts with the user through the `input()` function.

### 8. Mathematical Operations

The application performs calculations such as:

```text
Total Income
Total Expenses
Remaining Balance
```

---

## 📂 Project Structure

The current project can be organized as:

```text
Money-Manager/
│
├── money_manager.py
├── README.md
└── LICENSE
```

### File Description

| File               | Description             |
| ------------------ | ----------------------- |
| `money_manager.py` | Main Python application |
| `README.md`        | Project documentation   |
| `LICENSE`          | Project license         |

---

## ⚙️ Installation & Setup

### Step 1 — Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/YOUR-USERNAME/Money-Manager.git
```

Replace `YOUR-USERNAME` with your GitHub username.

---

### Step 2 — Navigate to the Project

```bash
cd Money-Manager
```

---

### Step 3 — Run the Program

Run:

```bash
python money_manager.py
```

If your system uses `python3`, run:

```bash
python3 money_manager.py
```

---

## ▶️ How to Use

### Step 1

Run the Python program.

### Step 2

Choose an option from the main menu.

For example:

```text
Enter your choice: 1
```

### Step 3

Enter your income:

```text
Enter income amount: ₹25000
```

### Step 4

Add your expenses:

```text
Enter expense amount: ₹1200
```

Then select the appropriate category.

### Step 5

Use the summary options to analyze your finances.

---

## 📊 Example Workflow

Suppose the user enters:

```text
Income:
₹25,000

Expenses:

Food          ₹3,000
Transport     ₹1,500
Shopping      ₹4,000
Education     ₹2,000
Entertainment ₹1,000
```

The program calculates:

```text
Total Income   : ₹25,000
Total Spending : ₹11,500
Remaining      : ₹13,500
```

Category summary:

```text
Food          : ₹3,000
Transport     : ₹1,500
Shopping      : ₹4,000
Education     : ₹2,000
Entertainment : ₹1,000
```

---

## 🔮 Future Improvements

The current version focuses on Python fundamentals. Several features can be added in future versions.

### 📁 Data Persistence

Store transactions in a file so that data remains available after the program closes.

Possible technologies:

* CSV
* JSON
* SQLite

### 📅 Date-Based Transactions

Add dates to income and expenses and allow users to filter transactions by:

* Day
* Week
* Month
* Year

### 💳 Income Categories

Add different income sources such as:

* Salary
* Freelancing
* Scholarship
* Pocket Money
* Other

### 🎯 Monthly Budget

Allow users to set a monthly spending limit.

Example:

```text
Monthly Budget: ₹15,000
Current Spending: ₹12,500

Budget Used: 83.3%

⚠ You are approaching your monthly budget.
```

### 💰 Savings Analysis

Calculate the user's savings:

```text
Savings = Income - Expenses
```

And savings percentage:

```text
Savings % = (Savings / Income) × 100
```

### 📈 Graphical Reports

Future versions could include charts showing:

* Monthly spending
* Category distribution
* Income vs expenses
* Savings trends

Libraries such as `matplotlib` could be used for this.

### 🖥️ Graphical User Interface

The command-line interface could eventually be converted into a desktop application using:

* Tkinter
* CustomTkinter
* PyQt

---

## 🎯 Project Objectives

The main objectives of Money Manager are:

1. Apply Python programming fundamentals to a real-world problem.
2. Understand how lists and dictionaries can store structured data.
3. Use functions to create modular programs.
4. Practice loops and conditional statements.
5. Perform calculations using user-provided data.
6. Build a menu-driven application.
7. Develop problem-solving and logical-thinking skills.
8. Create a practical project suitable for further development.

---

## 🌟 Why This Project?

Money Manager was selected because personal finance management is a common real-world problem.

Instead of creating a project that only demonstrates individual Python concepts, this project combines multiple concepts into a single functional application.

The project can also be expanded into a more advanced financial management system in the future.

---

## 🎓 Course Information

**Course:** Python Essentials
**Project:** Money Manager
**Project Type:** Python Console Application
**Domain:** Personal Finance Management

---

## 👨‍💻 Author

**Srikirti Bikram Paul**

B.Tech CSE Student

**Interests:** Python • AI/ML • Web Development • Software Engineering

---

## 📜 License

This project is created for educational purposes as part of a Python Essentials course project.

You are free to study, modify, and improve the project for learning purposes.

---

## ⭐ If You Like This Project

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

### 🚀 Future Vision

> **Money Manager starts as a simple Python expense tracker and can evolve into a complete personal finance management application with persistent storage, analytics, budgeting, visualization, and a graphical interface.**
