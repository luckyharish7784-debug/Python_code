class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return (f'employee salary {self.salary}')

class Manager(Employee):
    def __init__(self,name,bonus, salary):
        super().__init__(name, salary)
        self.bonus= bonus

    def calculate_bonus(self):
        return self.salary + self.bonus

class Developer(Employee):
    def __init__(self,name,overtime_pay, salary):
        super().__init__(name, salary)
        self.overtime_pay=overtime_pay

    def calculate_overtime(self):
        return self.salary + self.overtime_pay

mgr =  Manager('harish',5000,25000)
devp = Developer('Krish',10000,50000)

employee=[mgr,devp]

for i in employee:
    print(f'employee name {i.name} total payout {i.calculate_salary()}')
