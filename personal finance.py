import datetime


class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description="Income"):
        self.transactions.append({
            "type": "income",
            "amount": amount,
            "description": description,
            "date": datetime.datetime.now()
        })

    def add_expense(self, amount, description="Expense"):
        self.transactions.append({
            "type": "expense",
            "amount": -amount,  # Negative for expenses
            "description": description,
            "date": datetime.datetime.now()
        })

    def view_balance(self):
        balance = sum(transaction["amount"]
                      for transaction in self.transactions)
        print(f"\nCurrent Balance: ${balance:.2f}")

    def view_transactions(self):
        print("\nTransactions:")
        for transaction in self.transactions:
            date = transaction["date"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{date} | {transaction['type'].capitalize()}: ${
                abs(transaction['amount']):.2f} | {transaction['description']}")

    def view_summary(self):
        income = sum(transaction["amount"]
                     for transaction in self.transactions if transaction["type"] == "income")
        expenses = -sum(transaction["amount"]
                        for transaction in self.transactions if transaction["type"] == "expense")
        print("\nSummary:")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Net Savings: ${income - expenses:.2f}")


def main():
    tracker = FinanceTracker()

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. View Summary")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            amount = float(input("Enter income amount: $"))
            description = input("Enter income description: ")
            tracker.add_income(amount, description)
            print("Income added successfully.")
        elif choice == "2":
            amount = float(input("Enter expense amount: $"))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
            print("Expense added successfully.")
        elif choice == "3":
            tracker.view_balance()
        elif choice == "4":
            tracker.view_transactions()
        elif choice == "5":
            tracker.view_summary()
        elif choice == "6":
            print("Exiting the Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
