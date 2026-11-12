"""Functions that save expenses to file and read them back.

Date: 11 November 2026
Project: Expense Tracker
Student: Jimmy Morrison
Class: IT-566: Computer Scripting Techniques
"""

import csv
import json
import os

import expenses

# Name of the directory that holds data files
DATA_DIR = 'data'

# Default file name offered to the user
DEFAULT_JSON_FILENAME = 'expenses.json'
DEFAULT_CSV_FILENAME = 'expenses.csv'

# Column headings written to the first row of the CSV file
CSV_HEADINGS = ['Date', 'Category', 'Description', 'Amount']

# Top-level key in the JSON file
EXPENSES_KEY = 'expenses'


def get_data_dir_path():
    """Return the path to the data directory, creating it if needed."""
    working_dir = os.getcwd()
    # os.path.join uses the right slash for Windows or Mac.
    data_dir_path = os.path.join(working_dir, DATA_DIR)
    if not os.path.exists(data_dir_path):
        os.mkdir(data_dir_path)
    return data_dir_path


def save_expenses_to_json(expense_list, filename=DEFAULT_JSON_FILENAME):
    """Write a list of expenses to a JSON file and return the file path."""
    file_path = os.path.join(get_data_dir_path(), filename)

    data = {}
    data[EXPENSES_KEY] = expense_list

    # Convert the dictionary to JSON text. indent=4 makes it readable.
    json_string = json.dumps(data, indent=4)

    # "with" closes the file automatically when the block ends.
    with open(file_path, 'w') as f:
        f.write(json_string)

    return file_path


def read_expenses_from_json(filename=DEFAULT_JSON_FILENAME):
    """Read a JSON file and return its contents as a list of expenses."""
    file_path = os.path.join(get_data_dir_path(), filename)

    with open(file_path, 'r') as f:
        json_string = f.read()
    data = json.loads(json_string)

    expense_list = []
    # Rebuild each expense with create_expense so a file that
    # was edited by hand still gets checked.
    for item in data[EXPENSES_KEY]:
        expense = expenses.create_expense(item[expenses.DATE],
                                          item[expenses.CATEGORY],
                                          item[expenses.DESCRIPTION],
                                          item[expenses.AMOUNT])
        expense_list.append(expense)
    return expense_list


def export_expenses_to_csv(expense_list, filename=DEFAULT_CSV_FILENAME):
    """Write a list of expenses to a CSV file and return the file path."""
    file_path = os.path.join(get_data_dir_path(), filename)

    # newline='' stops Windows from adding a blank row between
    # every expense.
    with open(file_path, 'w', newline='') as f:
        # csv.writer puts quotes around values with commas, so
        # "Dinner, drinks" stays in one Excel cell.        
        writer = csv.writer(f)
        writer.writerow(CSV_HEADINGS)
        for expense in sorted(expense_list, key=expenses.get_expense_date):
            # The amount is written without a dollar sign so Excel
            # treats it as a number it can total.           
            writer.writerow([expense[expenses.DATE],
                             expense[expenses.CATEGORY],
                             expense[expenses.DESCRIPTION],
                             f'{expense[expenses.AMOUNT]:.2f}'])

    return file_path
