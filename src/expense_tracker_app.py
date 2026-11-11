"""Implements the Expense Tracker Application.

Date: 10 November 2026
Project: Expense Tracker
Student: Jimmy Morrison
Class: IT-566: Computer Scripting Techniques
"""

import os
import sys

import expenses


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
    
    def add_expense(self):
        """Prompt the user for a new expense and add it to the list."""
        print('\n\tAdd Expense\n')
        # If the date or amount is bad, create_expense raises an
        # error. The except shows a message and nothing is added.
        try:
            expense_date = input('\tDate (yyyy-mm-dd): ')
            category = input('\tCategory: ')
            description = input('\tDescription: ')
            amount = input('\tAmount: ')
            expense = expenses.create_expense(expense_date, category,
                                              description, amount)
            self._expenses.append(expense)
            print('\n\tExpense added.')
        except Exception as e:
            print(f'\n\tInvalid entry: {e}')
            print('\tExpense not added.')       

    def print_expenses(self):
        """Print all expenses to the console."""
        self.print_expense_report(self._expenses, 'All Expenses')

    def print_expense_report(self, expense_list, title):
        """Print a list of expenses as a table with a total."""
        print(f'\n\t{title}\n')
        if len(expense_list) == 0:
            print('\tThere are no expenses to print.')
            return

        print(f'\t{"Date":<12}{"Category":<16}{"Description":<30}'
              f'{"Amount":>10}')
        print(f'\t{"-" * 68}')
        # sorted() prints the expenses in date order without
        # changing the original list.
        for expense in sorted(expense_list, key=expenses.get_expense_date):
            print(f'\t{expenses.format_expense(expense)}')
        print(f'\t{"-" * 68}')
        total = expenses.calculate_total(expense_list)
        print(f'\t{"Total":<58}{total:>10.2f}')
        print(f'\t{len(expense_list)} expense(s)') 

    # The four methods below are stubs. They only print a message
    # for now. I will fill them in during Sprints 3 through 5.
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
