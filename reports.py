def monthly_summary(expenses):
    total = sum(e.amount for e in expenses)
    print(f"\nTotal Spent: ₹{total}")

def category_report(expenses):
    data = {}
    for e in expenses:
        data[e.category] = data.get(e.category, 0) + e.amount

    print("\nCategory Breakdown:")
    for k, v in data.items():
        print(f"{k}: ₹{v}")
