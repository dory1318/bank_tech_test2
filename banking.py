from datetime import datetime

class Account():
    def __init__(self):
        self.current_balance = 0

class Deposit():
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now().strftime("%d/%m/%Y")


class Withdraw():
    def __init__(self, amount):
        self.amount = amount
        self.date = datetime.now().strftime("%d/%m/%Y")
