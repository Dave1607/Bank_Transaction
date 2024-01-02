class Bank_Transactions():
    #initialize the bank class with the user'S name, account number and account balance 
    def __init__(self,name,account_number,account_balance):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    #uses user's account number as input to get the user details 
    def get_details(self,account_number):
        if isinstance(account_number, int) and account_number == self.account_number:
            return {'name':self.name,'account_number': self.account_number,'balance': self.account_balance}
        else:
            return {}
        
    def verify_user(self,name,account_number,balance):
        if (isinstance(name,str) and isinstance(account_number,int) and isinstance(balance,float)):
            get_user = self.get_details(account_number)
            if get_user != {}:
                if get_user['name']==name and get_user['account_number']==account_number and get_user['balance'] == balance:
                    return True
        return False
    
    #returns the user's account balance 
    def get_balance(self,account_number):
        if isinstance(account_number,int):
            get_user = self.get_details(account_number)
            if get_user != {}:
                if self.verify_user(
                    get_user['name'],
                    get_user['account_number'],
                    get_user['balance']
                    ):
                    return get_user['balance']

        return 'Please enter a valid account number'

    #process deposit transaction to the user's account
    def deposit(self,name,account_number,amount):
        if isinstance(name,str) and isinstance(account_number,int) and isinstance(amount,float):
            balance = self.get_balance(account_number)
            if self.verify_user(name,account_number,balance):
                self.account_balance += amount
                return 'Deposited Successfully'
            
        return 'Invalid Input! Please Enter valid details.'

    #process withdrawal transaction after verifying user's account balance 
    def withdrawal(self,name,account_number,amount):
        if isinstance(name,str) and isinstance(account_number,int) and isinstance(amount,float):
            balance = self.get_balance(account_number)
            if self.verify_user(name,account_number,balance):
                if amount <= balance:
                    self.account_balance -= amount
                    return 'Withdrawal Successful'
                else:
                    return 'Insufficient Balance'
                
        return 'Invalid Input! Please Enter Valid Details.'
            

    #process user's transfer request after check if the user has up to the requested amount 
    def transfer(self,sender_name, sender_account_number, receiver_name, receiver_account_number, amount,receiver_instance =None):
        if (
            isinstance(sender_name, str)
            and isinstance(sender_account_number, int)
            and isinstance(receiver_name, str)
            and isinstance(receiver_account_number, int)
            and isinstance(amount, float)
        ):
            if receiver_instance != None:
                sender_balance = self.get_balance(sender_account_number)
                
                # Get the receiver instance using receiver_account_number
                receiver = receiver_instance.get_details(receiver_account_number)
                receiver_balance = receiver.get('balance', 0.0)

                if amount <= sender_balance and receiver_instance.verify_user(receiver_name, receiver_account_number, receiver_balance):
                    self.withdrawal(sender_name, sender_account_number, amount)
                    receiver_instance.deposit(receiver_name, receiver_account_number, amount)
                    return "Transfer Completed"
                else:
                    return "Transfer Failed: Insufficient Sender Account Balance or Invalid Receiver Account Details"
            return "Invalid Transfer Details"
        return "Invalid Transfer Details"
