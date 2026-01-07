from .expense import Expense
from .expense_manager import ExpenseManager
from .file_handler import save_expenses, load_expenses
from .reports import monthly_summary, category_report

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.manager.expenses = load_expenses()

    def print_header(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

    def print_menu(self):
        print("\n" + "=" * 40)
        print("              MAIN MENU")
        print("=" * 40)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Generate Monthly Report")
        print("5. View Category Breakdown")
        print("6. Set/Update Budget")
        print("7. Export Data to CSV")
        print("8. View Statistics")
        print("9. Backup/Restore Data")
        print("0. Exit")
        print("=" * 40)

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        try:
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            desc = input("Enter description: ")

            expense = Expense(date, amount, category, desc)
            self.manager.add_expense(expense)
            save_expenses(self.manager.expenses)

            print("\nExpense added successfully!")
        except:
            print("\nInvalid input. Expense not saved.")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        if not self.manager.expenses:
            print("No expenses found.")
        else:
            for e in self.manager.expenses:
                print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

    def run(self):
        self.print_header()

        while True:
            self.print_menu()
            choice = input("\nEnter your choice (0-9): ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "4":
                print("\n--- MONTHLY REPORT ---")
                monthly_summary(self.manager.expenses)
            elif choice == "5":
                print("\n--- CATEGORY BREAKDOWN ---")
                category_report(self.manager.expenses)
            elif choice == "0":
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                break
            else:
                print("\nInvalid choice! Please enter 0-9.")
if __name__ == "__main__":
    app = FinanceTracker()
    app.run()