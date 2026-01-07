import json
import os
import shutil
from .expense import Expense

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"

def save_expenses(expenses):
    if os.path.exists(DATA_FILE):
        shutil.copy(DATA_FILE, BACKUP_DIR + "backup.json")

    with open(DATA_FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Expense.from_dict(x) for x in data]
