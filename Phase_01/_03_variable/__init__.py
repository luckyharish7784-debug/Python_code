"""
mutable : we can  modify or update the items(CRUD operations)
 ------>  list  set dict
immutable : we can't modify or update the items.
 ------>  int, float, complex, bool, tuple, none, string

iterable : which all the have unpacking capacity is known as iterable.
 ------> list, String, Set, Dict, Tuple
sequence : have index positions
 ------->  list string tuples
 unordered : set

 variable:
 --------
     variable is used to hold the value.
     variables should be meaningful for readability.

rules of variables:
--------------------
variable are start with alphabetic(a-z,A-Z),underscore('_') followed by Alphabetic('a-z','A-Z'0,digits(0-9)
underscore('_')

"""

#x= 10
# first check it is mutable or immutable
# if it is mutable then create one new memory address
# if it is immutable then check any allocated or not in memory location.


# x= 10
# #it is immutable datatype because integer we can't modify
# y = x+ 20
# print(x)
# print(y)

# s = 'developer'
# # for each in s:
# #     print(each)
# print(s)

# x=[1,2]
# y=[1,2]
# x={'a':1}
# y={'a':1}


# print(id(x))
# print(id(y))
'''
int,float,bool,complex,none,str,tuple --- all are same memory address
list, set, dict
'''
# print(10 and 200)
# x= 10
# y='hello'
# x=[10,52]
# print(x)
# print(y)
# print(x)

x,y,z= 10,'hii',{12,'ed',0}
print(x)
print(y)
print(z)