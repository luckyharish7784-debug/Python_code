# class Employee:
#     company_name = 'IBM'    #classvariable
#     company_address = 'Bangalore'
#     def __init__(self,employee_id,employee_name,employee_role):  #constructor
#         self.emp_id = employee_id          #instance variable
#         self.emp_name= employee_name
#         self.e_role  = employee_role
#
#     def employee_details(self):           #instance methods
#         return (f"employee id : {self.emp_id}\n"
#                 f"employee name : {self.emp_name}\n"
#                 f"employee role : {self.e_role}\n"
#                 f"company name : {Employee.company_name}\n"
#                 f"company_address : {Employee.company_address}\n")
#
#
#     @classmethod                       #classmethod
#     def company_details(cls):
#         return (f"company name : {cls.company_name}\n"
#                 f"company address : {cls.company_address}\n"
#                 # f"company Gate : {cls.Gate}\n"
#                 )
#
#     @staticmethod
#     def emi(EM):
#         return f"EMI or loan {EM}\n"
#
#
#
# obj=Employee(1230,'sai','Developer')
# print(obj)
# obj1=Employee(1229,'Krishna','Testing')
# print(obj1)
# print(obj.employee_details())
# print(obj.company_details())
# print(obj.emi(10000))
#
# print(obj1.employee_details())











class Employee:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal = sal

    def emp_details(self):
        return (f"name is {self.name} , age is {self.age} and salary is {self.sal}\n")
#
# obj=Employee('harish',25,50000.00)
# print(obj)
# obj.name='suresh'
# obj.loc='chennai'
# print(obj.loc)
# print(obj.emp_details())

# del obj.name
# print(obj.emp_details())   #it throws AttributeError

obj=Employee(24,'abh','xyz')
# print(obj)
obj.name=[10,20]
print(obj.name)







