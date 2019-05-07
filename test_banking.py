
from banking import *
import unittest

class TestAccount(unittest.TestCase):

    def test_account(self):
        bank = Account()
        balance = bank.current_balance
        self.assertEqual (balance, 0)

    def test_deposit_money(self):
        bank = Account()
        deposit = Deposit(1000, '10/01/2012')
        bank.deposit_money(deposit.amount, deposit)
        balance = bank.current_balance
        self.assertEqual (balance, 1000)

    def test_withdraw_money(self):
        bank = Account()
        deposit = Deposit(1000, '10/01/2012')
        bank.deposit_money(deposit.amount, deposit)
        withdraw = Withdraw(500, '14/01/2012')
        bank.withdraw_money(withdraw.amount)
        balance = bank.current_balance
        self.assertEqual (balance, 500)

    def test_puts_deposit_into_transaction_history(self):
        bank = Account()
        deposit = Deposit(1000, '10/01/2012')
        deposit2 = Deposit(2000, '13/01/2012')
        withdraw = Withdraw(500, '14/01/2012')
        bank.deposit_money(deposit.amount, deposit)
        bank.deposit_money(deposit2.amount, deposit2)
        bank.withdraw_money(withdraw.amount)
        transaction_history = bank.transaction_history
        self.assertEqual (transaction_history, [['date, withdraw, deposit, balance'], ["10/01/2012, 0, 1000, 1000"], ["13/01/2012, 0, 2000, 3000"], ["14/01/2012, 500, 0, 2500"]])


if __name__ == '__main__':
    unittest.main()
