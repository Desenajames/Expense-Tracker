# Expense-Tracker
A beginner friendly command line Expense Tracker built with Python. It lets you add, view, and delete your expenses and saves everything to a file so your data is never lost when you close the program
It allows users to add, view, delete expenses, and track total spending. All data is saved locally using a JSON file.

## 🎯 Objectives

The main objectives of this project are:

- To build a practical real-life expense tracking system
- To practice Python file handling using JSON
- To understand data persistence (saving and loading data)
- To implement CRUD operations (Create, Read, Update, Delete)
- To improve problem-solving skills using Python functions and loops
- To build a menu-driven command-line application

## 🛠️ Features

- Add new expenses with amount, category, and date
- View all saved expenses in a structured format
- Automatically calculate total spending
- Delete specific expenses
- Save data permanently using a JSON file
- Load previous expenses when program starts
- Simple and interactive CLI menu

## 📂 How It Works

1. The program loads existing expenses from `expenses.json`
2. User selects an option from the menu
3. Expenses are added, displayed, or deleted
4. All changes are automatically saved to file
5. Data persists even after closing the program

## 🚀 Future Improvements

- Add charts for expense tracking and analysis  
- Improve category system and filtering options  
- Replace JSON storage with a database (SQLite)  
- Add user login system  
- Create a GUI or web version  
- Add budget limits and alerts  

## 💾 Data Storage

- All expenses are stored in a local file: `expenses.json`
- Format used: JSON (lightweight data format)

Example structure:
```json
[
  {
    "amount": 50.0,
    "category": "Food",
    "date": "18-04-2026"
  }
]
