"""Implements the Expense Tracker Application.

Date: 10 November 2026
Project: Expense Tracker
Student: Jimmy Morrison (j0m94794@marymount.edu)
Class: IT-566: Computer Scripting Techniques
"""

import os
import sys


class ExpenseTrackerApp():
    """A menu-driven console application for tracking expenses."""

    # Named constants make the match statement easier to read.
    # Menu Choice Constants
    _ADD_EXPENSE = '1'
    _PRINT_EXPENSES = '2'
    _FILTER_EXPENSES = '3'
    _SAVE_EXPENSES = '4'
    _OPEN_EXPENSES = '5'
    _EXPORT_CSV = '6'
    _EXIT = '7'

    def __init__(self):
        """Initialize ExpenseTrackerApp object."""
        self._expenses = []

    def display_menu(self):
        """Print menu items to the console."""
        print('\n\t\tExpense Tracker Menu\n')
        print('\t1. Add Expense')
        print('\t2. Print Expenses')
        print('\t3. Filter Expenses')
        print('\t4. Save Expenses To File')
        print('\t5. Open Expense File')
        print('\t6. Export Expenses To CSV')
        print('\t7. Exit')

    def process_menu_choice(self):
        """Process menu commands."""
        menu_choice = ''
        # If the user presses Enter without typing, there is no first
        # character. The except keeps the program from crashing.
        try:
            user_input = input('\n\tEnter Command Number: ')
            menu_choice = user_input[0]
        except Exception:
            menu_choice = ''

        # Run the command that matches the number the user typed.
        # Anything else prints a warning.
        match menu_choice:
            case self._ADD_EXPENSE: self.add_expense()
            case self._PRINT_EXPENSES: self.print_expenses()
            case self._FILTER_EXPENSES: self.filter_expenses()
            case self._SAVE_EXPENSES: self.save_expenses()
            case self._OPEN_EXPENSES: self.open_expenses()
            case self._EXPORT_CSV: self.export_expenses()
            case self._EXIT: sys.exit()
            case _: self.print_error_message(menu_choice)

    # The six methods below are stubs. They only print a message
    # for now. I will fill them in during Sprints 2 through 5.
    def add_expense(self):
        """Prompt the user for a new expense and add it to the list."""
        print('\tAdd Expense is not implemented yet.')

    def print_expenses(self):
        """Print all expenses to the console."""
        print('\tPrint Expenses is not implemented yet.')

    def filter_expenses(self):
        """Filter expenses by date range and/or category."""
        print('\tFilter Expenses is not implemented yet.')

    def save_expenses(self):
        """Save expenses to a JSON file."""
        print('\tSave Expenses is not implemented yet.')

    def open_expenses(self):
        """Open a JSON expense file."""
        print('\tOpen Expense File is not implemented yet.')

    def export_expenses(self):
        """Export expenses to a CSV file."""
        print('\tExport Expenses is not implemented yet.')

    def print_status(self):
        """Display the number of expenses currently in memory."""
        print(f'\n\tExpenses in memory: {len(self._expenses)}')

    def print_error_message(self, menu_choice):
        """Warn of an invalid command entry."""
        print(f'\tWARNING: "{menu_choice}" is an invalid command!')

    def pause_program(self):
        """Wait for the user so output can be read."""
        input('\n\tPress Enter to continue... ')

    def clear_screen(self):
        """Clear the terminal window."""
        match(os.name):
            case 'posix':
                os.system('clear')
            case 'nt':
                os.system('cls')

    def start_application(self):
        """Start application processing loop."""
        # Keep showing the menu until the user picks Exit.
        while True:
            self.clear_screen()
            self.display_menu()
            self.print_status()
            self.process_menu_choice()
            self.pause_program()
