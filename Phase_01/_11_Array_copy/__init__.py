'''
req:
state: datatype/datastructure  input/output
beh : BL - CRUD - decision making loops operators

mutablIt is variable is declared inside the function, methods and block of code.
    list set dict  --- It is variable that is defined outside of any function or class .and can be accessed
immutable: once we can created then access only read,delete only. we can't update or modify.
    int float complex boolean none string tuple
Iterable: which going have unpacking capacity
     string list tuple set dict
sequence: which have the index position
      string list tuple range(range is a function)
unordered : set

variable:
It is used to stored or hold the values.
1.local variable  ---  It is variable is declared inside the function, methods and block of code.
2.global variable  --- It is variable that is defined outside of any function or class .and can be accessed   and modified
                        by any function.
3.non local variable ---

token= a token is a smallest unit of python program.
types of tokens.
1.keywords:-- keyword is a special meaning in python
              there are 35 keywords in python
2.identifers- It is used to variable name, function name and class name.
3.literals ---  it is a fixed value or constant in the programming language.
4.comment

Operators:
---------
Operators are symbols used to perform various operators on one or more operands.
Arithmetic = + - * % // / **
Comparsion = > < >= <= != <>
logical    = and or not
membership = in not in
assignment = += -= *= %= /= //= **=
identity   = is is not
bitwise    = and(&) or(|) xor(^)

datatypes:int,float , boolean,complex
datastructures:string, list, tuple, set, dict

string:
------
A string is a sequence of characters.
properties:
----------
1.Immutable
2.sequence(index)
3.ordered
4.iterable
5.'' or "" or '''''' or """ """
6.1114112 characters present in string
7.builtin -47

lower, upper, title, capitalize, swapcase, casefold
count,index,rindex,find,rfind,format,format_map
islower, isupper,istitle, isalpha,isalnum,isascii,isdigit,isnumeric,isdecimal,isidentifiers,isprintable,isspace
center , zfill,ljust,rjust
strip,lstrip,rstrip
split,rsplit,splitlines
startswith,endswith,removesuffix,removeprefix,partition,rpartition
join,replace,maketrans,translate,expandtabs,encode

list:
it is used to collection of elements
'''
'''
1.perfect square
2.perfect number

'''

'''0 1 1 2 3 5 8 
Fibnocci series'''

# num = int(input('enter number : '))
# res,res_1 =0,1
# for i in range(num):
#     print(res, end =' ')
#     res,res_1=res+res_1,res


# num = int(input('enter number : '))
# res,res_1=0,1
# i=0
# while i <=num:
#     print(res,end=' ')
#     res,res_1=res+res_1,res
#     i+=1

'''
 Given number is perfect number or not'''
# num=int(input('enter number : '))
# dup=num
# res=0
# for i in range(1,num):
#     if num%i==0:
#         res +=i
# if res==dup:
#     print('perfect number')
# else:
#     print('not perfect number')

'''
Given number is abundant number or not'''
#my number 12 -- LCM methods - It is divisible by 1,2,3,4,6(1+2+3+4+6 to add ) given number is greather than the add  number
#that is abundant number
#
# num=int(input('enter number : '))
# dup =num
# res=0
# for i in range(1,num):
#     if num%i==0:
#         res+=i
# if res>num :
#     print('abundant number')
# else:
#     print('not abundant number')


'''
Given number is perfect square or not'''

# num=int(input('enter number : '))
# square_num = int(num**0.5)
# if square_num * square_num == num:
#     print('Perfect square')
# else:
#     print('not perfect square')

'''Shallow copy'''
'''A shallow copy is creates a new object and insert references into it to the object found in original 
Syntax : copy.copy()'''
import copy
a=[[1,2],[3,4]]
b=copy.copy(a)

b[0][0]=99
print(id(b[0]))
print(id(a[0]))
#
# d={'a':10,'b':20,'c':[3,5]}
# d1=d
# d1['c'][0]=99
# print(id(d1))
# print(id(d))

# a={1,2,(6,8)}
# b=copy.deepcopy(a)
#
# print(a==b)
# print(a!=b)

a=[[1,45],[8,0]]
b=copy.deepcopy(a)

b[1][1] = 9
# print(id(a))
# print(id(b))
print(id(a[0]))
print(id(b[0]))