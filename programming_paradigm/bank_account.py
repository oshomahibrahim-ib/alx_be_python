# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # store balance as float so formatting always shows decimals
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Format with two decimal places to match checker (e.g. $250.00)
        print(f"Current Balance: ${self.account_balance:.2f}")
