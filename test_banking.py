
from banking import *
import unittest

class TestAccount(unittest.TestCase):
    def test_account(self):
        bank = Account()
        balance = bank.current_balance
        self.assertEqual (balance, 0)

    def test_deposit_money(self):
        bank = Account()
        deposit = Deposit(100)
        bank.deposit_money(deposit.amount)
        balance = bank.current_balance
        self.assertEqual (balance, 100)

    def test_withdraw_money(self):
        bank = Account()
        withdraw = Withdraw(50)
        bank.withdraw_money(withdraw.amount)
        balance = bank.current_balance
        self.assertEqual (balance, 50)

if __name__ == '__main__':
    unittest.main()
