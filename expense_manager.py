from .expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def list_expenses(self):
        return self.expenses

    def total_spent(self):
        return sum(e.amount for e in self.expenses)

    def by_category(self):
        result = {}
        for e in self.expenses:
            result[e.category] = result.get(e.category, 0) + e.amount
        return result
