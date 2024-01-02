# Bank Transactions Class

Welcome to the Bank Transactions Class! This Python class provides a simple implementation of basic banking transactions such as checking account details, verifying users, depositing, withdrawing, and transferring funds.

## Usage

To use this class, follow the steps below:

1. **Initialize the Bank Class:**
   ```python
   user_account = Bank_Transactions(name="John Doe", account_number=123456789, account_balance=1000.0)
   ```

2. **Get User Details:**
   ```python
   details = user_account.get_details(account_number=123456789)
   print(details)
   ```

3. **Verify User:**
   ```python
   is_verified = user_account.verify_user(name="John Doe", account_number=123456789, balance=1000.0)
   print(is_verified)
   ```

4. **Get Account Balance:**
   ```python
   balance = user_account.get_balance(account_number=123456789)
   print(balance)
   ```

5. **Deposit:**
   ```python
   deposit_result = user_account.deposit(name="John Doe", account_number=123456789, amount=500.0)
   print(deposit_result)
   ```

6. **Withdraw:**
   ```python
   withdrawal_result = user_account.withdrawal(name="John Doe", account_number=123456789, amount=200.0)
   print(withdrawal_result)
   ```

7. **Transfer:**
   ```python
   # Create another instance for the receiver
   receiver_account = Bank_Transactions(name="Jane Doe", account_number=987654321, account_balance=500.0)
   
   # Transfer funds from sender to receiver
   transfer_result = user_account.transfer(
       sender_name="John Doe",
       sender_account_number=123456789,
       receiver_name="Jane Doe",
       receiver_account_number=987654321,
       amount=100.0,
       receiver_instance=receiver_account
   )
   print(transfer_result)
   ```

## Contributions

Feel free to contribute to this project by submitting bug reports, feature requests, or improvements.

## Contact

If you have any questions or concerns, please reach out to [David Adikwu](https://twitter.com/dave_einstein_1) or open an issue in the [GitHub repository](https://github.com/Dave1607/Bank_Transaction).

Happy banking!
