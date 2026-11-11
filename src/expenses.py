"""Functions that create, validate, and format expenses.

Date: 10 November 2026
Project: Expense Tracker
Student: Jimmy Morrison
Class: IT-566: Computer Scripting Techniques
"""

from datetime import datetime

# Dictionary key names
# Using constants avoids typos in the key names.
DATE = 'date'
CATEGORY = 'category'
DESCRIPTION = 'description'
AMOUNT = 'amount'


def validate_date(date_string):
    """Return date_string in yyyy-mm-dd format or raise an Exception."""
    date_parts = date_string.strip().split('-')
    if len(date_parts) != 3:
        raise Exception('Date must be entered as yyyy-mm-dd.')
    # Building a datetime is the real check. Python raises an
    # error for a date that does not exist, like month 13.   
    try:
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
        valid_date = datetime(year, month, day)
    except Exception:
        raise Exception(f'"{date_string}" is not a valid date. '
                        'Use yyyy-mm-dd.')
    # strftime pads the month and day with zeros, so 2026-11-1
    # is stored as 2026-11-01.   
    return valid_date.strftime('%Y-%m-%d')


def validate_amount(amount_string):
    """Return amount_string as a positive float or raise an Exception."""
    cleaned_string = amount_string.strip().replace('$', '').replace(',', '')
    try:
        amount = float(cleaned_string)
    except Exception:
        raise Exception(f'"{amount_string}" is not a valid amount. '
                        'Enter a number such as 12.50.')
    if amount <= 0:
        raise Exception('Amount must be greater than zero.')
    return round(amount, 2)


# Every expense is built by this function, so every expense
# gets the same date and amount checks.
def create_expense(expense_date, category, description, amount):
    """Return a new expense dictionary built from validated values."""
    if not category.strip():
        raise Exception('Category cannot be blank.')
    expense = {}
    expense[DATE] = validate_date(expense_date)
    # title() saves food, FOOD, and Food all as "Food" so one
    # category does not end up with three spellings.   
    expense[CATEGORY] = category.strip().title()
    expense[DESCRIPTION] = description.strip()
    expense[AMOUNT] = validate_amount(str(amount))
    return expense


def get_expense_date(expense):
    """Return the date of an expense. Used as a sort key."""
    return expense[DATE]


def calculate_total(expense_list):
    """Return the sum of the amounts in a list of expenses."""
    total = 0.0
    for expense in expense_list:
        total += expense[AMOUNT]
    return round(total, 2)


def format_expense(expense):
    """Return an expense as one line of text in fixed-width columns."""
    return f'{expense[DATE]:<12}{expense[CATEGORY]:<16}' \
           f'{expense[DESCRIPTION]:<30}{expense[AMOUNT]:>10.2f}'