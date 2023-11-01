import tkinter as tk
from tkinter import messagebox

class BudgetTracker:
    def _init_(self, root):
        self.root = root
        self.root.title("Personal Budget tracker")

        self.income_label = tk.Label(root, text="Income:")
        self.income_label.grid(row=0, column=0, padx=10, pady=10)
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1)

        self.expense_label = tk.Label(root, text="Expense:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=10)
        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=1, column=1)

        self.add_income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=0, column=2, padx=10, pady=10)

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=1, column=2, padx=10, pady=10)

        self.balance_label = tk.Label(root, text="Balance: $0.00")
        self.balance_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.transactions_text = tk.Text(root, height=10, width=40)
        self.transactions_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.transactions = []

    def add_income(self):
        amount = float(self.income_entry.get())
        self.transactions.append(("Income", amount))
        self.update_balance(amount)
        self.update_transactions()

    def add_expense(self):
        amount = float(self.expense_entry.get())
        self.transactions.append(("Expense", -amount))
        self.update_balance(-amount)
        self.update_transactions()

    def update_balance(self, amount):
        current_balance = float(self.balance_label.cget("text")[10:])
        new_balance = current_balance + amount
        self.balance_label.config(text="Balance: $" + "{:.2f}".format(new_balance))

    def update_transactions(self):
        self.transactions_text.delete("1.0", tk.END)
        for transaction in self.transactions:
            transaction_type, amount = transaction
            formatted_amount = "{:.2f}".format(abs(amount))
            if amount > 0:
                transaction_str = f"+ {formatted_amount} ({transaction_type})\n"
            else:
                transaction_str = f"- {formatted_amount} ({transaction_type})\n"
            self.transactions_text.insert(tk.END, transaction_str)

if __name__ == "_main_":
    root = tk.Tk()
    app = BudgetTracker(root)
    root.mainloop()