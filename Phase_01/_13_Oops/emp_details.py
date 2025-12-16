class Employee:
    def __init__(self,name1,age,sal):
        print('from __init__ ')
        self.name =name1
        self._age=age
        self.sal=sal

    # def emp_details(self):
    #     return f"name is {self.name} , age is {self._age} and sal is {self.sal}\n"


    @property
    def name_details(self):
        return self._name

    @name_details.getter
    def name_get(self):
        print('from getter')

    @name_get.setter
    def name_set(self,name_value):
        print('from setter')
        if not isinstance(name_value,str):
            raise ValueError ("name must  be a string")
        self._name = name_value

    @name_set.deleter
    def name_details(self):
        print('from deleter')
        del self.name




obj=Employee(34,25,50000)
print(obj.name_get)
# obj1=Employee('hari',34,5000.00)
# print(obj.emp_details())
# print(obj1.emp_details())
