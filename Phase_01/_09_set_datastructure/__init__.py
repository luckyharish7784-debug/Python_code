'''
set :
---
A Set is a collection of distinct (unique) elements.

properties:
----------
1.Mutable-once we can use crud after create also it can update or modify of the elements.
   -- list set dict
2.Unordered :
3.iterable: which goto have unpacking capacity.
  --- str list tuple set dict
4.set is represented by
  --> If it is empty set --- set()
  --> if it is element set -- {element,}
5.Unique,only immutable
6.builtin methods - 17

Builtin methods:
----------------
adding : add
removing : pop remove discard  clear
union     intersection          difference         symmetric_difference
update    intersection_update   difference_update  symmetric_difference_update
isdisjoint issubset issuperset
copy



1.add:
------
It is used to add the element at end of the set.
s={1,2.3,4j,False}
print(s.add(5))

2.remove:
--------
it is used to remove the specified element in the set
s={1,2,3,4}
s.remove(3)
print(s)    === output:{1,2,4}

s = {1,2,3,4}
s.remove(5)
print(s) ====output: It throws error (keyerror)

3.discard::
-----------

'''
#
# s = {1, 2.3, 4j, False}
# s.add((9,0))
# print(s)

# s = {1, 2.3, 4j, False}
# s.add({9,0})
# print(s)  --- IT THROUGH ERROR

# s = {1,2,3,4}
# s.remove(3)
# print(s)
# s={1,2.3,3j,True,None,'Python',(22,44)}
# s.remove('P')
# print(s)

# s={1,2,3}
# res= s * 2
# print(res)

# s=[1,2,2,3]
# emp=set(s)
# print(s)
#
# s={7,2,5}
# for each in s:
#     print(each)

# s1={1,2,3}
# s2={4,5}
# s=s1.union(s2)
# print(s)

# s1={1,2,3}
# s2={4,5}
# s3={each for each in s1}|{each_1 for each_1 in s2}
# print(s3)

# res = s1 | s2
# print(res)

# s1={1,2.5,45}
# s2={2.5,4.5,'py'}
# res=s1.union(s2)
# # # res_1=s1.difference(s2)
# # s1.difference(s2)
# # print(s1)
# print(res)

# s={1,2,3}
# # s.add(4)
# s.add('py')
# print(s)

# s={7,8,'p',99,10}
# res=s.remove(8)
# s.remove('py')
# s.pop()
# # print(res_1)
# print(s)

# s={2.5,3j,0,True,None,'python',(3,'pi'),55}
# s.pop()
# # s.remove('pi')
# print(s)

# s={1,2,3}
# s1={2,3,4}
# res=s.intersection(s1)
# print(res)

# s={12,(1,3)}
# s.add(2)
# print(s)

ls=[1,2,(3,4)]
# ls.append(5)
# x=ls.append(5)  #None
# print(x)
# print(ls)
# ls.extend('hii')
# x=ls.extend('hii')  #output = None
# print(x)
# x=ls.insert(89,2)  #None
# ls.insert(2,[2,889])
# print(ls)

# my_set = {1, 2, 3}
# my_set.discard() #it's through TypeError
# my_set.discard(4)   #it will return same set output.
# my_set.discard(3)
# print(my_set)

# my_set = {1, 2, 3}
# # my_set.remove()  # it's through error
# # my_set.remove(0)   # TypeError
# my_set.remove(2)
# print(my_set)

#
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# # s=set1.symmetric_difference_update(set2)   #None
# set1.symmetric_difference_update(set2)
# print(set1)

# s={1,2,3}
# s.add(4)
# print(s)
# a=s.add(5)
# print(a)
# s.add({'a':2,'b':4})
# print(s)   #TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')


# s={}
# # s.remove(4)
# x=s.pop()
# print(x)

# s={1,2,3,4}
# s.discard(3)
# print(s)
# x=s.discard(3)
# print(x)
# s={}
# s.discard()
# print(s)














