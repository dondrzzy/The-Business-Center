import unittest
from bank_account import BankAccount, MinimumBalanceAccount
 
class AccountBalanceTestCase(unittest.TestCase):
	def setUp(self):
		self.my_account = BankAccount()

	def test_balance(self):
		self.assertEqual(self.my_account.balance, 3000, msg='Account Balance Invlalid')

	def test_deposit(self):
		self.my_account.deposit(4000)
		self.assertEqual(self.my_account.balance, 7000, msg='Deposit methods unsuccessful')

	def test_withdraw(self):
		self.my_account.withdraw(2000)
		self.assertEqual(self.my_account.balance, 1000, msg='Withdraw method Invlalid')

	def test_invalid_transaction(self):
		self.assertEqual(self.my_account.withdraw(6000), "Insufficient balance", msg='Insufficient balance')

	def test_subclass(self):
		self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not Subclass')