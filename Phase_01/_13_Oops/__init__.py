'''
class:
------
class is a blueprint for creating objects.

object:
-------
object is a realtime entity .

Encapsulation
Instance variable
Instance method
class method
static method
property method
constructor
private instance variable
private instance methods
protect instance variable
protect instance method
'''

class Bank:
    Bank_name = 'SBI' # class variable
    ROI = 10

    def __init__(self,Name,Mob_no):   #constructor
        self.name= Name     #instance variable
        self.mob_no=Mob_no

    # def __str__(self):
    #     return f"name {self.name} and mobile {self.mob_no}"
    def account_details(self):     #instance Method
        return (f"Bank Name : {Bank.Bank_name}\n"
                f"account holder name : {self.name}\n"
                f"mobile number : {self.mob_no}\n"
                f"Bank name  : {Bank.Bank_name}\n")


    @classmethod  #we can't access instance variable & instance methods
    def bankname(cls):
        return (f"Bank name : {Bank.Bank_name}\n"
                # f"Account name : {cls.name}\n"   -- Attribute Error
                # f"Account name : {self.name}\n"   -- NameError
                )

    @staticmethod
    def rate_of_interest ():
        return f"Bank loan interset {Bank.ROI}"






obj=Bank('Harish',7997476016)
print(obj)
obj1=Bank('Krishna',7032864628)
print(obj1)
print(obj.account_details())
print(obj.rate_of_interest())

print(obj.bankname())
#