# class Employee:
#     def __init__(self,name,age,sal):
#         print('from __init__ ')
#         self.name =name
#         self._age=age
#         self.sal=sal
#
#     # def emp_details(self):
#     #     return f"name is {self.name} , age is {self._age} and sal is {self.sal}\n"
#
#
#     @property
#     def name_details(self):
#         return self._name
#
#     @name_details.getter
#     def name_details(self):
#         print('from getter')
#         return f"from the Getter {self._name}"
#
#
#     @name_details.setter
#     def name_details(self,name_value):
#         print('from setter')
#         if not isinstance(name_value,str):
#             raise ValueError ("name must  be a string")
#         self._name = name_value
#
#
#     # @name_details.deleter
#     # def name_details(self):
#     #     print('from deleter')
#     #     del self.name
#
#
#
#
# obj=Employee(20,25,50000)
# # print(obj.name_details)
# # print(obj.name_get)
# # # obj.name_details="rakesh"
# # # print(obj.name_details)
# # # obj.name_details=12
# # print(obj.name_details)
# # del obj.name_details
# # obj.name_details='hello'
# # print(obj.name_details)


# class Employee:
#     def __init__(self,name1,age,sal):
#         print('from __init__ ')
#         self.name =name1
#         self._age=age
#         self.sal=sal
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.getter
#     def name(self):
#         print('from getter')
#         return f"from the Getter {self._name}"
#
#     @name.setter
#     def name(self, name_value):
#         print('from setter')
#         if not isinstance(name_value, str):
#             raise ValueError("name must  be a string")
#         self._name = name_value
#
#     @name.deleter
#     def name(self):
#         print('from deleter')
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.getter
#     def age(self):
#         print('from getter age')
#         return self._age
#
#     @age.setter
#     def age(self,age_value):
#         print('from age setter')
#         if not isinstance(age_value,int):
#             raise ValueError ('age is must be integer')
#         self._age=age_value
#
#     @age.deleter
#     def age(self):
#         print('from age deleter')
#         return self._age
#
# obj = Employee('harish','abd','fhu')
# # print(obj.name)
# # del obj.name
# # obj.age= 'adb'
# # print(obj.age)
# obj.age=24
# print(obj.age)

#
# class A:
#     def in_meth(self):
#         return "from A"
#
# class B(A):
#     def in_meth(self):
#         return "from B"
#
# class C(B):
#     def in_meth(self):
#         return "from C"
#
# obj1=A()
# obj2=B()
# obj3=C()
# print(obj1.in_meth())
# print(obj2.in_meth())
# print(obj3.in_meth())
#

