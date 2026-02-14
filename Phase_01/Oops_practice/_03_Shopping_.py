'''
3. Online Shopping Cart
Entities:
•	Item: Represents a product with a name and price.
•	Cart: Holds the list of items and manages the checkout process.
•	Discount: Represents various types of discounts.
Steps:
1.	Item Class:
a.	Attributes: name, price.
b.	Methods: get_price(), which returns the price of the item.
2.	Cart Class:
a.	Attributes: items (a list of Item objects), discount.
b.	Methods:
i.	add_item(item): Adds an item to the cart.
ii.	set_discount(discount): Sets a discount strategy for the cart.
iii.	calculate_total(): Calculates the total price, applying the discount if available.
3.	Discount Class:
a.	Methods: apply_discount(total): Abstract method to be implemented by subclasses.
b.	Subclasses:
i.	PercentageDiscount: Reduces the total by a percentage.
ii.	FixedDiscount: Reduces the total by a fixed amount.
4.	Polymorphism:
a.	The apply_discount() method in Cart is called based on the type of discount selected.
Example Problem:
•	Create a cart, add items, apply a discount, and calculate the total amount.

'''


'''Online shopping Cart'''
# from abc import ABC, abstractmethod
# 
# 
# class Item:
#     def __init__(self,name,price):
#         self.name =name
#         self.price = price
# 
#     def get_price(self):
#         return self.price
# 
# class Cart:
#     def __init__(self):
#         self.items = []
#         self.discount = None
# 
#     def add_item(self,item):
#         self.items.append(item)
# 
#     def set_discount(self,discount):
#         self.discount = discount
# 
#     def calculate_total(self):
#         total_bal = 0
#         for each in self.items:
#             total_bal += each.get_price()
#         if self.discount:
#             total_bal = self.discount.apply_discount(total_bal)
#         return total_bal
#         # subtotal = sum(i.get_price() for i in self.items)
#         #
#         # if self.discount:
#         #     final_total = self.discount.apply_discount(subtotal)
#         # else:
#         #     final_total = subtotal
#         # return final_total
# 
# class Discount(ABC):
#     @abstractmethod
#     def apply_discount(self,total):
#         pass
#
# 
# class Per_discount(Discount):
#     def __init__(self,percentage):
#         self.percentage = percentage
# 
#     def apply_discount(self,total):
#         reduction = total * (self.percentage / 100)
#         return total - reduction
# 
# class Fix_discount(Discount):
#     def __init__(self,amount):
#         self.amount = amount
# 
#     def apply_discount(self,total):
#         return max(0,total - self.amount )
# 
# 
# # 1. Setup Items and Cart
# laptop = Item("Laptop", 1000)
# mouse = Item("Wireless Mouse", 50)
# my_cart = Cart()
# 
# my_cart.add_item(laptop)
# my_cart.add_item(mouse)
# #
# # ten_percent = Per_discount(10)
# # my_cart.set_discount(ten_percent)
# # print(f"Total: ${my_cart.calculate_total():.2f}")
# 
# hundred_off = Fix_discount(100)
# my_cart.set_discount(hundred_off)
# print(f"Total: ${my_cart.calculate_total():.2f}")
# 
# #=============================================================================================================
# 
# class Item:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         self.total=0
# 
#     def get_price(self):
#         print (f'Product price {self.price} ')
# 
# class Cart:
#     def __init__(self):
#         self.item=[]
#         self.discount=None
# 
# 
#     def add_item(self,item):
#        self.item.append(item)
# 
#     def set_discount(self,discount):
#         self.discount = discount
# 
#     def calculate_total(self):
#         total = 0
#         for each in self.item:
#             total = total + each.get_price()
# 
#         if self.discount :
#             total = self.discount.fix_dis(total)
#         return total
# 
# 
# class Discount:
#     def __init__(self,total):
#         raise NotImplementedError('Subclass method is implemented')
# 
# class per_dis(Discount):
#     def __init__(self,total,percentage):
#         super().__init__(total)
#         self.percentage = percentage
# 
#     def total_amount(self,total):
#         return total - (total * self.percentage  /100)
# 
# class fix_dis(Discount):
#     def __init__(self, amount, total):
#         super().__init__(total)
#         self.amount = amount
# 
#     def total_dis(self,total):
#         return max(0,total - self.amount)
# 
# # Create items
# item1 = Item("Laptop", 50000)
# item2 = Item("Mouse", 1000)
# 
# # Create cart
# cart = Cart()
# cart.add_item(item1)
# cart.add_item(item2)
# 
# # Apply discount
# discount = per_dis(0,10)   # 10% discount
# cart.set_discount(discount)
# 
# # Calculate total
# print("Total Amount:", cart.calculate_total())
# 

#==================================================================================================
# class PrivateClass:
#     def __init__(self):
#         self.__private_variable = None
#
#     def priv_fun(self):
#         # self.__private_variable = "I am private variable in instance method"
#         print(self.__private_variable)
#
#
# priv_obj = PrivateClass()
# # Accessing private variable will result in an AttributeError
# # print(priv_obj.__private_variable)
# print(PrivateClass().__private_variable)
# priv_obj.priv_fun()

# class ProtectedClass:
#
#     def __init__(self):
#         self._protected_variable = "I am protected variable"
#
#
#     def pro_fun(self):
#         # self._protected_variable = "I am protected variable in instance method"
#         print(self._protected_variable)
#
#
# pro_obj = ProtectedClass()
# print(pro_obj._protected_variable)
# print(ProtectedClass()._protected_variable)
# pro_obj.pro_fun()
#

# l=[1,2,3,4,5]
# sum=0
# res=[]
# for i in range(0,len(l),1):
#     sum = l[i]+l[i+1]
#     res.append(sum)
# print(res)

# s='  the sky  is blue '


# reverse = s.split()
# return ''.join
# m=reverse[::-1]
# res=''
# for i in m:
#     res = res + ' ' + i

# print(res)
x=2000-1000
y=1000
a,b=500,500
z=a+b
print(id(x),id(y),id(z))

