from datetime import datetime

class Account():
    def __init__(self):
        self.current_balance = 0
        self.transaction_history = [['date, withdraw, deposit, balance']]

    def deposit_money(self, amount, deposit):
        self.current_balance += amount
        self.puts_deposit_into_transaction_history(deposit)

    def withdraw_money(self, amount, withdraw):
        self.current_balance -= amount
        self.puts_withdraw_into_transaction_history(withdraw)

    def puts_deposit_into_transaction_history(self, deposit):
        self.transaction_history.append([f"{deposit.date}, 0, {deposit.amount}, {self.current_balance}"])

    def puts_withdraw_into_transaction_history(self, withdraw):
        self.transaction_history.append([f"{withdraw.date}, {withdraw.amount}, 0, {self.current_balance}"])

class Deposit():
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date


class Withdraw():
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

class CurrentTime():
    def __init__(self):
        self.date = datetime.now().strftime("%d/%m/%Y")
