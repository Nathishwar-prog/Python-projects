

```markdown
# Basic Expense Tracker CLI

A simple command-line expense tracker written in Python that helps you record and analyze your daily expenses.

## Features

- **Add Expenses**: Record expenses with amount, category, and optional description
- **View History**: See all recorded expenses in chronological order
- **Expense Summary**: Get a breakdown of spending by category
- **Data Persistence**: Expenses are automatically saved to a JSON file

## Installation

1. Ensure you have Python 3.x installed
2. Clone this repository or download the `expense_tracker.py` file

## Usage

Run the program with:

```bash
python expense_tracker.py
```

### Menu Options

1. **Add Expense**:
   - Enter the amount spent
   - Specify a category (e.g., Food, Transport)
   - Add an optional description
   - The expense is automatically timestamped

2. **View Expenses**:
   - See all recorded expenses with details
   - Expenses are shown in chronological order

3. **View Expense Summary**:
   - Get a category-wise breakdown of spending
   - See your total expenses

4. **Exit**:
   - Quit the application

## Data Storage

All expenses are stored in `expenses.json` in the same directory. The file is automatically created when you add your first expense.

## Example Usage

```
Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. View Expense Summary
4. Exit

Enter your choice (1-4): 1
Enter amount spent: 15.50
Enter category (e.g., Food, Transport, Entertainment): Food
Enter a brief description (optional): Lunch at cafe
Expense added successfully!
```

## Requirements

- Python 3.x
- No external dependencies required
