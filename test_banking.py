
from banking import *
import unittest

class TestAccount(unittest.TestCase):
    def test_account(self):
        bank = Account()
        balance = bank.current_balance
        self.assertEqual (balance, 0)

if __name__ == '__main__':
    unittest.main()
