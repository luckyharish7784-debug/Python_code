'''
req :
----
state : datatype/data structure input/output
beh   : BL decision_making,oops, operators, CRUD

mutable : we can modify or update the items
          list set dict
immutable : we can't modify or update in the items
           int, float, complex, boolean , str, tuple
iterable  : which have unpacking capacity
           list set str tuple dict
sequence : which have the index value or position
          str list tuple
unordered : set


list:
----
1.mutable
2.iterable
3.sequence
4.ordered
5.[]
6.homogenous and heterogeneous
7.built in methods - 11

tuple :
-----
1.immutable
2.ordered
3.sequence
4.iterable
5.()
6.homogenous and heterogeneous
7.built in methods - 2

set :
----
1.mutable
2.unordered
3.iterable
4.set(),{elements}
5.duplicates are not allowed





'''

# s = [1,3.5,4j,1,'hii',True,[5,6],(66,77),{44,'a'},{10:7,9:'i'}]
# print(s)

# s = (12,1.3,14j,True,1,'hii',[6,9],('g',4),{66,'a'},{10:7,9:'i'})
# print(s)

s = {12,1.3,14j,True,1,'hii',('g',4)}
print(s)


