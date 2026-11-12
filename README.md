# Expense Tracker

IT-566 Project 2. A multi-module Python console application that lets users enter, filter, and print expenses.

## Tasks:
* Write a multi-module Python application that lets users enter, filter, and print expenses to the console.
* Save expense data to file in JSON format
* The application must be able to open expense files
* The application must also be able to export expense data to CSV format so it can be opened in Microsoft Excel
* Filter expenses by date range and/or category

## How to Run

Python 3.10 or newer is required. From the project folder, run:

    python src/main.py

On Windows in Git Bash, use `winpty python src/main.py` instead.

## Menu Commands

1. Add Expense: enter a date (yyyy-mm-dd), category, description, and amount
2. Print Expenses: show all expenses in date order with a total
3. Filter Expenses: show expenses within a date range and/or category
4. Save Expenses To File: save to a JSON file in the data folder
5. Open Expense File: open a saved JSON file
6. Export Expenses To CSV: create a CSV file that opens in Excel
7. Exit

## Modules

* main.py: starts the program
* expense_tracker_app.py: the menu and all user input and output
* expenses.py: creates and checks expenses
* expense_file_ops.py: saves and opens JSON files, exports CSV
* expense_filters.py: filters by date range and category

## Status

All five sprints are complete and have been verified by me.

## AI Assistance

I used AI as a learning and guidance tool throughout this project, primarily to help me understand Python concepts, explore why certain approaches worked, and clarify the reasoning behind the code. I also used Computer Scripting Techniques with Python (First Edition) by Rick Miller (Pulp Free Press) as a supporting learning resource and reference.

The project was developed over three days across five structured sprints. I personally wrote every line of code, created all comments, and implemented each feature myself. AI was used to support my understanding and learning, not to generate the project's code.

At the end of each sprint, I tested my work, reviewed the results, and committed the completed changes before moving on to the next stage. This iterative approach allowed me to build the project incrementally while developing a deeper understanding of Python, the individual components, and how the overall program works together.

My goal was not simply to build a working program, but to use the development process to strengthen my Python skills, apply what I was learning, and understand the code I was writing.
