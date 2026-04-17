import unittest
from methods import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Bob", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(30), 70)
        with self.assertRaises(ValueError):
            self.account.withdraw(200)
        with self.assertRaises(ValueError):
            self.account.deposit(-10)


if __name__ == '__main__':
    unittest.main()

