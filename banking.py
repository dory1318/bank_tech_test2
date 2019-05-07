from datetime import datetime

class Account():
    def __init__(self):
        self.current_balance = 0

    def deposit_money(self, amount):
        self.current_balance += amount

    def withdraw_money(self, amount):
        self.current_balance -= amount

class Deposit():
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now().strftime("%d/%m/%Y")


class Withdraw():
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now().strftime("%d/%m/%Y")
