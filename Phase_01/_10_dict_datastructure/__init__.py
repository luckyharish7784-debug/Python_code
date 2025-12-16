'''
req:
----
state:datatype/ds input/output
beh: business logic -crud,decision making , loops, operators

mutable: we can create after use modify or update the object.
        list set dict
immutable: we can't update or modify in the object/element.
           int float complex bool str tuple
iterbale: which going have unpacking capcity
          str list tuple set dict range
sequence : str list tuple range
unordered = set

operators:
---------
Arithmetic operator = + - * % // / **
comparison operator = > < >= <= <> !=
logical operator    = and or not
membership operator = in notin
assignment operator = += -= *= %= //= /= **=
identity operator   = is is not
bitwise operator    = &(and)  |(or) ~(not)  ^(xor)


dictionary properties:
--------------------
1.mutable--we can access CRUD
2.mapping type
3.ordered (version 3.17+)
4.iterable -- which going have unpacking capacity
5.key - unique ,only immutable datatype
6.value - both mutable and immutable
7.{keys : values}
8.builtin - 11

Builtin methods:
------------------
clear, pop , popitem,setdefault, from keys, key, value, items ,update, gets, copy

adding - update
removing - pop , popitem, clear,
keys - key , fromkey
values - value ,
remaining - items, gets, setdefault, copy
'''

# d={'a':1,'b':3}
# # x=d.setdefault('b',4)
# # print(x)    #output = 4
# # d.setdefault('b',4)
# # print(d)   #output={'a':1,'b':4}
# d.setdefault('c')
# print(d)

# d={'a':1,'b':2,'c':3}
# # d1={'b':3,'c':4,'d':5}
# d2={}
# # d.update(d1)
# # print(d)   #'a': 1, 'b': 3, 'c': 4, 'd': 5}
#
# # d2=d.update(d1)
# # print(d2)   #None
#
# d.update(d2)
# print(d)


# d={'a':1,'b':2,'c':3}
# # d.pop('c')
# # print(d)
# # x=d.pop('c')
# # print(x)
# d.pop(3)
# print(d)

# d={'a':1,'b':2}
# d1=d.get('c')
# print(d1)

# d={'a':1,'b':2,'c':3}
# # d.keys()
# # print(d)
# m=d.keys()
# print(m)

# d=['a','b','f']
# m=dict.fromkeys(d)
# print(m)
d={'a','b','f'}
m=dict.fromkeys(d,[8,9])
print(m)

'''1.Count Characters 
Problem: Count the frequency of each character in a string. 
Input: "hello" 
Expected Output: {'h':1, 'e':1, 'l':2, 'o':1}'''

# user_input = input('enter a string : ')
# empty_dict ={}
# for ele in user_input:
#     if ele in empty_dict:
#         empty_dict[ele]+=1
#     else:
#         empty_dict[ele]=1
# print(empty_dict)

#=====================================================================================

'''2.Check Anagram 
Problem: Check if two strings are anagrams using dictionaries.
 Input: {"listen": "silent"} 
 Expected Output: True
'''

# input_dict = {'listen':'sileNt'}
# key1=list(input_dict.keys())[0]  #[0] fetches that one item.
# value1=list(input_dict.values())[0] #[0] fetches that one item.
#
# key1=key1.lower()
# value1=value1.lower()
# if len(key1) != len(value1):
#     print(False)
# else:
#     count1 = {}
#     count2 = {}
#     for ele in key1:
#         if ele in count1:
#             count1[ele] += 1
#         else:
#             count1[ele] = 1
#     for ele1 in value1:
#         if ele1 in count2:
#             count2[ele1] += 1
#         else:
#             count2[ele1] = 1
#
#     print(count1 == count2)

#=======================================================================================

'''
14.Dict to List of Tuples 
Problem: Convert dictionary to list of (key, value). 
Input: {'x':1, 'y':2} 
Expected Output: [('x',1), ('y',2)]'''

# inp_dict={'x':1,'b':2}
# res=[]
# for key in inp_dict:
#     value=inp_dict[key]
#     dump=(key,value)
#     res.append(dump)
#
# print(res)
#=========================================================================================
'''50.Dictionary Symmetric Difference 
Problem: Get keys only in one of two dictionaries but not both, ignoring values. 
Input: {'a':1, 'b':2}, {'b':3, 'c':4} 
Expected Output: {'a', 'c'}
'''
# dict = {'a':1,'b': 2}
# dict2={'b':3 ,'c': 4}
#
# keys1=set(dict.keys())
# keys2=set(dict2.keys())
#
# sym_differ = (keys1 ^ keys2)
#
# print(sym_differ)


''' without builtin method'''

# dict={'a':1,'b':2,'d':1}
# dict2={'b':3,'c':4}
# res=[]
# for key in dict:
#     if key not in dict2:
#        res.append(key)
# for key1 in dict2:
#     if key1 not in dict:
#         res.append(key1)
#
# empt_dict = set(list(res))
#
# print(empt_dict)

# dict={'a':1,'b':2,'d':1}
# dict2={'b':3,'c':4}
# res=[]
# for key in dict:
#     if key not in dict2:
#        res+=[key]
# for key1 in dict2:
#     if key1 not in dict:
#         res+= [key1]
#
# empt_dict = set(res)
#
# print(empt_dict)

#=======================================================================================

'''
49. Recursive Key Capitalization 
Problem: Capitalize all keys recursively in nested dictionary. 
Input: {'a': {'b': 1} } 
Expected Output: {'A': {'B': 1} }
'''
# inp_output = {'a':{'B':1}}

# ls=[1,2,3,4]
# l1=['a','b','c','d']
# print(zip(ls,l1))  ===== output zip memory address object




# print(chr(ord('a')-32))

# ========================================================================================

# inp={'listen':'silent'}
# key1=list(inp.keys())[0]
# value1=list(inp.values())[0]
#
#
# key1 = key1.lower()
# value1=value1.lower()
#
# if len(key1) == len(value1):
#     count={}
#     count1={}
#     for ele in key1:
#         if ele in count:
#             count[ele]+=1
#         else:
#             count[ele]=1
#     for ele1 in value1:
#         if ele1 in count1:
#             count1[ele1]+=1
#         else:
#             count1[ele1]=1
#     print(count == count1)
#
# else:
#     print(False)

#==========================================================================
'''
3.Merge Dictionaries 
Problem: Merge two dictionaries; keys don’t overlap.
 Input: {'a':1}, {'b':2} 
Expected Output: {'a':1, 'b':2}'''
# dt1={'a':1}
# dt2={'b':2}
# dt1.update(dt2)
# print(dt1)

#=================================================================================

'''
4.Dictionary from Lists 
Problem: Make a dictionary from two lists—keys and values. 
Input: ['a', 'b'], [1, 2] 
Expected Output: {'a':1, 'b':2}'''
#
# inp_1=['a','b']
# inp_2 = [1,2]
#
# emp_dict={}
# for ele in range(len(inp_1)):
#     emp_dict[inp_1[ele]]=inp_2[ele]
# print(emp_dict)

#======================================================================
'''
Key Exists or Not 
Problem: Check if a key exists inside the dictionary. 
Input: {'x': 5}, key 'x' 
Expected Output: True'''

# data = {'x':5}
# key = input('enter a key : ')         # i will change input but it returns different output.
# for ele in data:
#     if ele == key:
#         print(True)
# else:
#     print(False)

#===========================================================================

'''. Find Max Value Key 
Problem: Find the key with the highest value. 
Input: {'a':5, 'b':10, 'c':3}
 Expected Output: 'b'  '''

# inp_dict = {'a':5,'b':10,'c':3}
#
# for ele in inp_dict:
#     if inp_dict[ele] <

'''Nested Dictionary Lookup 
# Problem: Lookup a nested key given a list of keys. 
# Input: d={'a':{'b':{'c':10}}}, keys=['a','b','c']
# Expected Output: 10'''
#
# # input={'a':{'b':{'c':10}}}
# # keys=['a','b','c']
# # output=input     #Start with value = d
# # for ele in keys:  #For each key in keys, go one level deeper:
# #     output=output[ele]      #1.value = value['a'] → {'b':{'c':10}}
#                                #value = value['b'] → {'c':10}
#                                #value = value['c'] → 10
# # print(output)

# d={'a':{'b':{'c':{'d':10}}}}
# keys=['a','b','c']
# dup=d
# for ele in keys:
#     dup= dup[ele]
# print(dup)
'''=================================================================================='''

# d={'a':10,'b':5,'c':20}
# #excepted output={'a':10,'c':20}
# empt={}
# tar=10
# for value in d:
#     if d[value] >= tar:
#         empt[value]=d[value]
# print(empt)

'''========================================================================================'''

# d={'a':2,'b':3}
# d1={'a':3,'c':4}
#
# output={}
# for ele in d:
#     output[ele]=d[ele]
# for ele1 in d1:
#     if ele1 in output:
#         output[ele1]+=d1[ele1]
#     else:
#         output[ele1]=d1[ele1]
# print(output)

#=====================================================================================\

'''
Count number of consecutive blocks of same character. 
Input: "aaabbba" 
Expected Output: {'a':2, 'b':1}'''

# data="aaaabbba"
# dict={}
# res=''
# for char in data:
#     if char != res:
#         dict[char]=dict.get(char,0)+1
#         print(dict)
# #         res=char
# # print(dict)

# data='aaaabbbaadb0ccc'
# output={}
# for char in range(len(data)):
#     if char == 0 or data[char]!=data[char-1]:
#         if data[char] not in output:
#             output[data[char]] =1
#         else:
#             output[data[char]] += 1
# print(output)



#=========================================================================================================

'''
Problem: Group words by their length.
Input: ['a', 'cat', 'bat', 'dog', 'be'] 
Expected Output: {1: ['a'], 2: ['be'], 3: ['cat', 'bat', 'dog']}'''

# s=['a','cat','bat','dog','be']
# output={}
# for ele in s:
#     len_char=len(ele)
#     if len_char not in output:
#         output[len_char]=[]
#         print(output)
#     output[len_char].append(ele)
# print(output)

#==========================================================================================================================
# s='hello'
# d={}
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] = d[i]+ 1
# print(d)

'''
Find keys that appear in two dictionaries with same values. 
Input: {'a':1, 'b':2}, {'a':1, 'b':3}
 Expected Output: ['a']'''

# d1={'a':1,'b':2}
# d2={'a':3,'c':4}
# empty=[]
# for key in d1:
#     if key in d2:
#         empty += [key]
# print(empty)

'''
Merge two dictionaries summing values for common keys. 
Input: {'a':2, 'b':3}, {'a':3, 'c':4} 
Expected Output: {'a':5, 'b':3, 'c':4}'''
# def stg_func(d1,d2):
#     output={}
#     for key in d1:
#         output[key]=d1[key]
#     for key1 in d2:
#         if key1 in output:
#             output[key1]=output[key1]+d2[key1]
#         else:
#             output[key1]=d2[key1]
#     return output
#
# print(stg_func({'a':2,'b':3},{'a':3,'c':4}))

#====================================================================================

'''
Find keys that differ between two dictionaries. 
Input: {'x':5,'y':10}, {'y':10,'z':15} 
Expected Output: ['x', 'z']'''

# d={'x':5,'y':10}
# d1={'y':10,'z':15}
# output=[]
# for ele in d:
#     if ele not in d1:
#         output=output + [ele]
# for ele1 in d1:
#     if ele1 not in d:
#         output = output+[ele1]
#
# print(output)

#=============================================================================================

'''
Find top 2 keys with highest values.
 Input: {'a':5, 'b':10, 'c':3} 
Expected Output: ['b', 'a']'''
#
# d={'a':5,'b':10,'c':3}
# res=[]
# for

#==================================================================================================

'''
Sum values greater than 5. 
Input: {'a': 3, 'b': 7, 'c': 6} 
Expected Output: 13'''

# data = {'a':3,'b':7,'c':6}
# value=5
# total=0
# for ele in data:
#     if data[ele]>value:
#         total = total + data[ele]
# print(total)

#=====================================================================================

'''
Find keys for a given value. 
Input: {'cat': 1, 'dog': 2, 'bird': 1}, value = 1 
Expected Output: ['cat', 'bird']'''

# data={'cat':1,'dog':2,'bird':1}
# value=1
# res=[]
# for ele in data:
#     if data[ele] == value:
#         res = res+[ele]
# print(res)


#========================================================================================

'''
Problem: Remove items with value None. 
Input: {'a': 1, 'b': None} 
Expected Output: {'a':1}'''

# d={'a':1,'b':None}
# output={}
# for ele in d:
#     if d[ele] != None:
#         output[ele]=d[ele]
# print(output)

#===================================================================================

'''
Find keys missing from dictionary compared to reference keys. 
Input: {'a':1, 'b':2}, reference ['a','c','b'] 
Expected Output: ['c']'''
#
# d={'a':1,'b':2}
# ref=['a','b','c']
# res=[]
# for ele in ref:
#     if ele not in d:
#         res = res+[ele]
# print(res)

#===================================================================================

'''
Remove keys starting with 'a'. 
Input: {'apple':1, 'banana':2, 'avocado':3} 
Expected Output: {'banana':2}'''

# d={'apple':1,'banana':2,'avocado':3}
# output={}
# for key,value in d.items():
#     if not key.startswith('a'):
#         output[key]=value
#
# print(output)

# d={'apple':1,'banana':2,'avocado':3}
# out={}
# for key,value in d.items():
#     if len(key)>0 and key[0]!='a':
#         out[key]=value
# print(out)




# l=[10,20,30,50,40]
# m=max(l)
# res=[]
# for ele in l:
#     if ele < m:
#         res.append(ele)
# n=max(res)
# print(n)

# s='python is  fun     '
# char=''
# res=[]
# for i in s:
#     if i != ' ':
#         char += i
#
#     elif char != ' ':
#         res.append(char)
#         char=''
# m=len(res)
# print(m)


# def fun_dic(d1,d2):
#     empty=[]
#     for key in d1:
#         if key in d2:
#             empty += [key]
#     return empty
# d1={'a':1,'b':2}
# d2={'b':3,'c':4}
# print(fun_dic(d1,d2))


# def fun_dict(d):
#     res=0
#     m=list(d.values())
#     emp=''
#     dup=m[0]
#     for ele in m:
#         if ele>dup:
#             res=ele
#     for i in d:
#         if d[i]==res:
#             emp += i
#     return emp
# d={'Alice':90,'Bob':91,'Charlie':95}
# print(fun_dict(d))

# s='python is fun'
# count=0
# count1=0
# for char in s:
#     if char in 'aeiouAEIOU':
#         count+=1
#     elif 'a'<= char <= 'z' or 'A'<=char<='Z':
#         count1 += 1
# print(count)
# print(count1)

# l1 = [1, 2, 3, 4]
#
# # output list with 1s
# output = [1] * len(l1)
#
# # Step 1: prefix product
# prefix = 1
# for i in range(len(l1)):
#     output[i] = prefix
#     prefix *= l1[i]
#
# # Step 2: suffix product
# suffix = 1
# for i in range(len(l1)-1, -1, -1):
#     output[i] *= suffix
#     suffix *= l1[i]
#
# print(output)

a = [10, 20, 30, 40, 50,90]
#
# # a.remove(10)
# # print("After remove(30):", a)
#
# popped_val=a.pop(100)
# print("Popped element:", popped_val)
# print("After pop(1):", a)


# d={'a':10,'b':20}
# d.items() #it's return the same dictionary
# s=d.items()
# print(s)

# d.keys()    #it's return the same dictionary
# s=d.keys()
# print(s)

# d={'a':10,'b':20,'d':5}
# value=tuple(d.values())
# dup=value[0]
# res=[]
# for ele in d:
#     if d[ele] > dup:
#         res += [ele]
# print(res)


# d={'a':10,'b':2}
# d.pop('d')  #it return Keyerror
# d.pop()    #it return typeError
# m=d.pop('b')
# print(d)

# d={'a':10,'b':100,}


