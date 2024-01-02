import unittest
from Bank_System import Bank_Transactions

class TestBankTransactions(unittest.TestCase):

    def setUp(self):
        # Initialize a sample account for testing
        self.bank_account = Bank_Transactions(name="John Doe", account_number=123456, account_balance=1000.0)

    def test_get_details(self):
        details = self.bank_account.get_details(123456)
        self.assertEqual(details, {'name': 'John Doe', 'account_number': 123456, 'balance': 1000.0})

        details_invalid = self.bank_account.get_details(654321)
        self.assertEqual(details_invalid, {})

    def test_verify_user(self):
        self.assertTrue(self.bank_account.verify_user("John Doe", 123456, 1000.0))
        self.assertFalse(self.bank_account.verify_user("Jane Doe", 123456, 500.0))
        self.assertFalse(self.bank_account.verify_user("John Doe", 654321, 1000.0))
        self.assertFalse(self.bank_account.verify_user("John Doe", 123456, 2000.0))

    def test_get_balance(self):
        balance = self.bank_account.get_balance(123456)
        self.assertEqual(balance, 1000.0)

        invalid_balance = self.bank_account.get_balance(654321)
        self.assertEqual(invalid_balance, 'Please enter a valid account number')

    def test_deposit(self):
        result = self.bank_account.deposit("John Doe", 123456, 500.0)
        self.assertEqual(result, 'Deposited Successfully')
        self.assertEqual(self.bank_account.account_balance, 1500.0)

        invalid_result = self.bank_account.deposit("John Doe", 654321, 200.0)
        self.assertEqual(invalid_result, 'Invalid Input! Please Enter valid details.')
        self.assertEqual(self.bank_account.account_balance, 1500.0)

    def test_withdrawal(self):
        result = self.bank_account.withdrawal("John Doe", 123456, 200.0)
        self.assertEqual(result, 'Withdrawal Successful')
        self.assertEqual(self.bank_account.account_balance, 800.0)

        insufficient_result = self.bank_account.withdrawal("John Doe", 123456, 1000.0)
        self.assertEqual(insufficient_result, 'Insufficient Balance')
        self.assertEqual(self.bank_account.account_balance, 800.0)

        invalid_result = self.bank_account.withdrawal("John Doe", 654321, 200.0)
        self.assertEqual(invalid_result, 'Invalid Input! Please Enter Valid Details.')
        self.assertEqual(self.bank_account.account_balance, 800.0)

    def test_transfer(self):
        # Setting up a second account for testing transfer
        receiver_account = Bank_Transactions(name="Jane Doe", account_number=654321, account_balance=500.0)

        transfer_result = self.bank_account.transfer("John Doe", 123456, "Jane Doe", 654321, 300.0,receiver_account)
        self.assertEqual(transfer_result, 'Transfer Completed')
        self.assertEqual(self.bank_account.get_balance(123456), 700.0)

        # Create a separate receiver instance to verify its balance
        receiver_balance = receiver_account.get_balance(654321)
        self.assertEqual(receiver_balance, 800.0)

        invalid_result = self.bank_account.transfer("John Doe", 123456, "Janet Doe", 987654, 200.0)
        self.assertEqual(invalid_result, 'Invalid Transfer Details')
        self.assertEqual(self.bank_account.get_balance(123456), 700.0)

        # Verify the receiver's balance again
        receiver_balance = receiver_account.get_balance(654321)
        self.assertEqual(receiver_balance, 800.0)



if __name__ == '__main__':
    unittest.main()
