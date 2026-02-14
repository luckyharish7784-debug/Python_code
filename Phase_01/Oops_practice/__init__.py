'''
Online Banking System
Entities:
•	Account: Represents a bank account with attributes like account holder and balance.
•	SavingsAccount: A specific type of account with an interest rate.
•	CheckingAccount: Another type of account that allows overdraft.
Steps:
1.	Account Class:
a.	Attributes: account_holder, balance (initially set to 0).
b.	Methods:
i.	deposit(amount): Increase the balance by the deposit amount.
ii.	withdraw(amount): Decrease the balance if the amount is available.
iii.	get_balance(): Return the current balance.
2.	Inheritance:
a.	SavingsAccount and CheckingAccount inherit from Account.
b.	SavingsAccount:
i.	Adds an interest_rate and has a method to calculate interest: calculate_interest().
c.	CheckingAccount:
i.	Adds an overdraft_limit and overrides withdraw() to allow withdrawals even if the balance is negative (up to the overdraft limit).
3.	Encapsulation:
a.	Balance should be protected (private) to prevent direct modification outside the class. Use getter and setter methods to interact with the balance.
Example Problem:
•	Create a SavingsAccount and CheckingAccount, deposit funds into them, and calculate interest or withdraw within the overdraft limit.

'''


class Account:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.__balance = 0

    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f'deposit successfully Rs.{self.__balance}')
        else:
            print('Invalid amount')

    def withdraw(self,amount):
        if self.__balance > 0 and amount >0: # 0 < amount <= self.balance
            self.__balance -= amount
            print(f'Available balance in your account Rs.{self.__balance}')
        else:
            print('Insufficient Balance in your account')

    def get_balance(self):
        return self.__balance

    def _set_balance(self,amount):
        self.__balance = amount

class SavingsAccount(Account):
    def __init__(self,account_holder,interest):
        super().__init__(account_holder)
        self.interest = interest

    def calculate_interest(self):
        intrst = self.get_balance() * self.interest
        print(f'Interest calculate : ${intrst:.2f}')
        return intrst

class CheckingAccount(Account):
    def __init__(self,account_holder,overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):
        avail_amount = self.get_balance() + self.overdraft_limit
        # new_amount =self.get_balance()
        if 0<amount <= avail_amount :
            new_bal = self.get_balance() - amount
            self._set_balance(new_bal)
            print(f"Withdrew ${amount}. Current Balance: ${new_bal}")
        else:
            print("Withdrawal exceeds overdraft limit.")


#savingsaccount
# savings = SavingsAccount("Alice", 0.05) # 5% interest
# savings.deposit(1000)
# interest = savings.calculate_interest()
# savings.deposit(interest)

#checkingaccount
checking = CheckingAccount('Krish',500)
checking.deposit(1000)
checking.withdraw(200)
checking.withdraw(900)
checking.withdraw(900)
