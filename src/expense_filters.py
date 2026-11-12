"""Functions that filter a list of expenses.

Date: 11 November 2026
Project: Expense Tracker
Student: Jimmy Morrison
Class: IT-566: Computer Scripting Techniques
"""

import expenses


def filter_by_date_range(expense_list, start_date='', end_date=''):
    """Return the expenses dated from start_date through end_date."""
    # ISO dates compare correctly as text, so no date math is
    # needed. An empty string means no limit on that side.
    filtered_list = []
    for expense in expense_list:
        if start_date != '' and expense[expenses.DATE] < start_date:
            continue
        if end_date != '' and expense[expenses.DATE] > end_date:
            continue
        filtered_list.append(expense)
    return filtered_list


def filter_by_category(expense_list, category):
    """Return the expenses in the given category."""
    # Compare in lowercase so food, Food, and FOOD all match.
    wanted_category = category.strip().lower()
    filtered_list = []
    for expense in expense_list:
        if expense[expenses.CATEGORY].lower() == wanted_category:
            filtered_list.append(expense)
    return filtered_list


def filter_expenses(expense_list, start_date='', end_date='', category=''):
    """Return expenses filtered by date range and/or category."""
    filtered_list = filter_by_date_range(expense_list, start_date, end_date)
    # Only apply the category filter if the user typed a category.
    if category.strip() != '':
        filtered_list = filter_by_category(filtered_list, category)
    return filtered_list


def get_categories(expense_list):
    """Return each category in use once, in alphabetical order."""
    categories = []
    for expense in expense_list:
        if expense[expenses.CATEGORY] not in categories:
            categories.append(expense[expenses.CATEGORY])
    categories.sort()
    return categories
