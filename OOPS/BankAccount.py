from InsufficientFunds import InsufficientFundsException

class BankAccount:
    def __init__(self, acc_holder, acc_num, balance=0):
        self.acc_holder = acc_holder
        self.acc_num = acc_num
        self.balance = balance

    def deposit(self, amt):
        if amt<=0:
            raise ValueError("Deposit must be positive")
        self.balance += amt
        print(f"Deposited {amt} New balance:{self.balance}")

    def withdraw(self,amt):
        if amt<=0:
            raise ValueError("Withdraw amount must be positive")
        if amt>self.balance:
            raise InsufficientFundsException("Not enough balance")
        self.balance -= amt
        print(f"Withdrawn {amt}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance
    
# Usage
try:
    account = BankAccount("Nihal", "2XXX567", balance=5000)
    print(f"Account holder: {account.acc_holder}\n Balance: {account.balance}")
    account.deposit(700)
    account.withdraw(1500)
    account.withdraw(4500)

except InsufficientFundsException as e:
    print(f"Failed Transaction: {e}")
except Exception as e:
    print(f"Error occured: {e}")