
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

if __name__ == '__main__':
    unittest.main()
