# class Bank:
#     def __init__(self,name,balance=0):
#         self.name=name
#         self._balance=balance
#
#
#     def deposit(self,amount):
#         # amount = int(input('enter amount : '))
#         if amount >0:
#             self._balance += amount
#             print(f"deposited amount {self._balance}")
#         else:
#             print('invalid deposit amount ')
#
#     def withdraw(self,amount):
#         if amount > self._balance:
#             self._balance -= amount
#             print(f'withdraw amount {amount}')
#             print(f'current balance {self._balance}')
#         else:
#             print("Insufficient Balance")
#
#     def get_balance(self):
#         return {self._balance}
#
#
# class Saving_account(Bank):
#     def __init__(self,name,interest_rate):
#         super().__init__(name)
#
#         self.interest_rate = interest_rate
#
#     def calculate_intrst(self):
#         intrst= self._balance * (self.interest_rate / 100)
#         return intrst
#
# class CheckingAccount(Bank):
#     def __init__(self,name,overdraft_limit):
#         super().__init__(name)
#         self.limit = overdraft_limit
#
#     def acc_withdraw(self,amount):
#         if amount >= self._balance + self.limit:
#             new_balance = self._balance - amount
#             self._balance = new_balance
#             print(f"withdraw {amount}")
#
#         else:
#             print('Insufficient Balance in your account')
#             # print('over draft limit exceeded')
# savings = Saving_account("Ravi", 5)
# savings.deposit(10000)
# print("Savings Balance:", savings.get_balance())
# print("Interest:", savings.calculate_intrst())
#
# print("-" * 30)
#
# # Create Checking Account
# checking = CheckingAccount("Suresh", 5000)
# checking.deposit(2000)
# checking.acc_withdraw(6000)   # overdraft allowed
# print("Checking Balance:", checking.get_balance())


# class Account:
#     def __init__(self,account_holder,balance=0):
#         self.name = account_holder
#         self._balance = balance
#
#     def deposit(self,amount):
#         if amount > 0:
#             self._balance = self._balance + amount
#             print(f'current account balance is {self._balance}')
#         else:
#             print('Invalid amount')
#
#     def withdraw(self,amount):
#         if amount > 0 and self._balance > 0:
#             self._balance -= amount
#             print(f'Remaining Balance is {self._balance}')
#         else:
#             print('Insufficient Balance in your account')
#
#     def get_balance(self):
#         return self._balance
#
#
# class SavingAccount(Account):
#     def __init__(self,account_holder,intrst_rate):
#         super().__init__(account_holder)
#         self.intrst_rate = intrst_rate
#
#     def calculate_intrst(self):
#         intrst= self._balance * (self.intrst_rate / 100)
#         return intrst
#
# class CheckingAccount(Account):
#     def __init__(self,account_holder,overdraft_limit):
#         super().__init__(account_holder)
#         self.limit = overdraft_limit
#
#     def withdraw(self,amount):
#         if amount <= self._balance + self.limit :
#             new_balance = self._balance - amount
#             self._balance=new_balance
#             print(f'remaining balance is {self._balance}')
#         else:
#             print(f'Insufficient Balance in your account')
#
#
# #saving Account
#
# saving = SavingAccount('harish',5)
# saving.deposit(10000)
# print('after deposit amount is present in my account ')
# saving.withdraw(1000)
# # print(saving)
#
# print('-' * 30)
#
# #checking Account
# checking = CheckingAccount('babu',1000)
# checking.deposit(4000)
# checking.withdraw(1000)






















