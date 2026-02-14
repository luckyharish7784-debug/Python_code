'''
list:
mutable
sequence
ordered
iterable
[]
all dt/ds
homogenous and heterogenous data

builtin methods - 11

builtin methods:
--------0------

adding : append , extend , insert
removing : pop , remove, clear
common : count, index
remaining : sort, reverse, copy


tuple:
-----
immutable
sequence
ordered
iterable
(),(element,)
all dt/ds
homogenous and heterogenous data

builtin methods - 2

builtin methods:
---------------
count ,index




difference between list and tuple
          list                |                        tuple
 1.list is a mutable datatype   |  1. Tuple is a immutable datatype
2.It is declared by square         2. It is declared by currley brackets -().(element,)
brackets -[]                    |
3. It takes more memory space   |  3. It takes less memory space
4.A List is a variable
  memory location               |  4.A Tuple is a fixed memory location
                                |
list comprehension:
   provides a concise and readable way to create a new list based on the values of an existing iterable

   synatx: ls = [expression for variable in iterables ifcondition(optional)]

list convensions:
   list(iterables)
'''
from itertools import count

# #    -10 -9  -8  -7   -6    -5      -4     -3     -2           -1
# # ls = [10,2.5,5j,True,None,'hello',[11,20],(1,3),{11,15},{'a':99,'c':True}]
# #      0  1   2   3    4     5       6      7      8            9
# # # print(ls[::])
# # print(ls[1:len(ls):])
#
# # ==============================================================================
#
# # s='_Hello+world='
# # x=s.strip()
# # print(x)
# # ls = [10,2.5,5j,True,None,'hello',[11,20],(1,3),{11,15},{'a':99,'c':True}]
# # start=int(input('enter number : '))
# # end=int(input('enter number : '))
# # step=int(input('enter number : '))
# # print(ls[start:end:step])
#
# # ====================================================================================
#
# # #    -10 -9  -8  -7   -6    -5      -4     -3     -2           -1
# # ls = [10,2.5,5j,True,None,'hello',[11,20],(1,3),{11,15},{'a':99,'c':True}]
# # #      0  1   2   3    4     5       6      7      8            9
# # ls.append(0)
# # print(ls)
#
# # =============================================================================================
#
# '''
# * * * * *
# * * * *
# * * *
# * *
# *
# '''
# # n=int(input('enter number : '))
# # for each in range(n):
# #     print('*' * (n-each))
#
# #==========================================================================
#
# # st = [1,2,2,3]
# # emp=[]
# # for each in st:
# #     if each not in emp:
# #         emp =[each] + emp
# # print(emp)
#
# #output = [3,2,1]
# #==============================================================================
#
# # ls = [1,2,2,3]
# # emp = []
# # for each in ls:
# #     if each not in emp:
# #         emp += [each]
# # print(emp)
#
# # ls=[1,2,2,3]
# # emp = []
# # start = 1
# # while start <len(ls):
# #     if  start not in emp:
# #         emp += [start]
# #     start +=1
# # print(emp)
#
# #====================================================================================================
# # ls=['cat','dog']
# # empt=[]
# # for each in ls:
# #     empt = empt+[each[-1::-1]]
# # print(empt)
# # ======================================================================================================
#
# # ls1=[1,3,5]
# # ls2=[2,4,6]
# # #
# # # for each in ls2:
# # #     ls1= ls1 + [each]
# # #
# # # print(ls1)
# # empt=[ls1+ls2]
# # print(empt)
# #======================================================================================
# ls=[5,3,8,1,34,3454]
# max_value = ls[0]
# for each in ls:
#     if each>max_value:
#         max_value = each
# res=max(ls)
# print(res)
#
# #==========================================================================================
#
# # Rotate List Right by k
#
# # ls=[1,2,3,4,5]
# # input_1=2
# # emp=[]
# # for each in ls:
# #     if each > (input_1+1):
# #         emp=emp+[each]
# # print(emp)

#==========================================================================

# ls=[1,2,3,4,5]
# # k=2
# # output_ls = []
# # res=[]
# # emp=[]
# # for i in ls:
# #     if i>(k+1):
# #         res += [i]
# #     elif i<=(k+1):
# #         emp += [i]
# # output_ls = output_ls+res+emp
# # print(output_ls)

#========== (or) =============================

# ls=[1,2,3,4,5]
# k=2
# for each in range(k):
#     last = ls[-1]
#     for each_1 in range(len(ls)-1,0,-1):
#         ls[each_1] = ls[each_1-1]
#     ls[0]=last
# print(ls)

# ==========================================================================
#
# ls=[3,1,2,3,2]
# emp=[]
# for each in ls:
#     if each not in emp:
#         emp.append(each)
# print(emp)

#======================================================================

# ls=[1,2,3,4,5]
# sum=5
# res=[]
# for each in ls:
#     for e_ch in range(len(ls)):
#         e_ch=ls[e_ch]
#         if each < e_ch:
#             if sum == (each+e_ch):
#                 res += [(each,e_ch)]
# print(res)

#===========================================================================
# ls=[1,2,3,4,5]
# target=9
# res=[]
#
# for start in range(len(ls)):
#     for each in range(start+1,len(ls)):
#         for e_ch in range(each+1,len(ls)):
#             if target == ls[start]+ls[each]+ls[e_ch]:
#                 res = [ls[start],ls[each],ls[e_ch]]
# print(res)


#===========================================================================
#
# ls=[1,2,5]
# num=5
# res=[]
# for each in range(1,num+1):
#     if each not in ls:
#         res += [each]
# print(res)
#====================================================================
# ls=[1,2,7,9]
# # x=[i for i in range(min(ls),max(ls)+1) if i not in ls]
# # print(x)

# s=[3,1,2,3,2]
# res=list(dict.fromkeys(s))
# print(res)

# ================================================================
# s=[1,3,2,4,5,7]
# # x=s.append(8)
# # x=s.insert(5,[2,6])
# # x=s.extend()
# # s.remove()  #if any argument not provide through typeerror
# # s.remove(-1) # if i give one argument but that element is not present in list, it's through valueError
# # x=s.pop()     # if out of range or index, it's through IndexError
# s.clear(1)    #if any argument provide through typeError.
# s.clear()
# # print(x)
# print(s)


#====================================================================

# s=[1,4,6,7,8,4]
# res=0
# for i in s:
#     res += i
# print(res)
# print(sum(s))

# ls=[2,3,4,5,2,7,11,15]
# # #o/p=[2,3,5,2,7,11]
# res=[]
# for each in ls:
#     num=each
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         res += [each]
# print(res)



# n=int(input('enter number : '))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('prime')
# else:
#     print('not prime')

# import keyword
# print(keyword.kwlist)

# l = [1, 2, 3, 4, 5]
# target = 9
# ls=[]
# for i in l:
#     total = 0
#     for j in range(i, len(l)):
#         total += l[j]
#         if total == target:
#              ls.append(l[j])
#              break
# print(ls)

# nums = [1, 2, 3, 4, 5]
# target = 9
# is_bool=True
# for i in range(len(nums)):
#     total = 0
#     for j in range(i, len(nums)):
#         total += nums[j]
#         if total == target:
#             print(nums[i:j+1])
#             break


# ls=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# res=[]       # Create empty list in global declaration
# for i in ls:
#     output= [] # create one more empty list in global declaration
#     for j in range(len(i)):
#         output.append(ls[j][i])
#     else:
#         res.append(output[ : :-1])
# print(res)


# ls=[2,3,4,5,6,7,8,10,10]
# m=max(ls)
# res=[]
# for i in ls:
#     if i< m:
#         res.append(i)
# n=max(res)
# print(n)

# s=['flower','flow','flight']
# r=""
# x=zip(*s)
# for i in x:
#     if len(set(i))==1:
#         r+=i[0]
# print(r)
#
# d = {'a': 1, 'b': 2,'c':23}
# # x=d.popitem()
# x=d.pop('')
# print(d)
# print(x)
#
# l = [10, 20, 30, 20,1]
# # l.remove()
# l.pop()
# print(l)

# ls=[2,3,4,6,7]
# if ls == sorted(ls):
#     print('ascending')
# else:
#     print('not')



# x=[1,2,3]
# m=x.append(6)
# print(m)
# print(x)
#
# m=lst.insert(1, 15)
# print(m)
# lst = []
# lst.insert(1,'a')
# print(lst)

lst = [10, 20, 30,20]
# # lst.extend(10)
# # lst.extend('adp')
# lst.extend("{'a':10,'b':20}")
# print(lst)
# lst.pop(1)
# lst.remove(20)
# x=lst.remove(20)
# print(lst)
# print(x)

# l=['gyuj','ttg5huj7j7j5yqq525y','bhrfrr','hcr5yhyhbe']
# m=sorted(l,key=len)
# print(m)






