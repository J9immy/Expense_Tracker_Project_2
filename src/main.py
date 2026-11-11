"""Serves as the point of entry to the Expense Tracker Application.

Date: 10 November 2026
Project: Expense Tracker
Student: Jimmy Morrison
Class: IT-566: Computer Scripting Techniques
"""

from expense_tracker_app import ExpenseTrackerApp


def main():
    """Execute main program."""
    expense_tracker_app = ExpenseTrackerApp()
    expense_tracker_app.start_application()


if __name__ == '__main__':
    main()