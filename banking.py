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

    def show_transaction_history(self):
        for i in self.transaction_history:
            print(",".join(i).replace(",", " || "))


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


date = CurrentTime()
account = Account()
deposit = Deposit(1000, date.date)
deposit2 = Deposit(2000, date.date)
withdraw = Withdraw(400, date.date)
account.deposit_money(deposit.amount, deposit)
account.deposit_money(deposit2.amount, deposit2)
account.withdraw_money(withdraw.amount, withdraw)
account.show_transaction_history()
