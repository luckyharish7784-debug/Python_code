'''
function:
--------
function are a block of statement that does a specific task.
there are 2 types of function.
1.defining function
2.calling function

1.defining function:

    syntax: def function_name(parameters):
                   block of statements

2.calling function:

      syntax: def function_name(parameters):
                   block of statements
'''
from itertools import count

'''Prime number'''
#
# def fun_prime(num):
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count == 2 :
#         return 'prime number'
#     else:
#         return 'not prime number'
#
# x=fun_prime(2)
# print(x)

# '''Armstrong number '''
# def fun_armstrong(num):
#     l=len(str(num))
#     dup=num
#     res=0
#     while dup>0:
#         digit = dup%10
#         res= res + digit**l
#         dup//=10
#     if res==num:
#         return 'armstrong'
#     else:
#         return 'not armstrong'
# print(fun_armstrong(int(input('enter number : '))))

# s='the quick brown fox'
#output=['the','quick','brown','fox']
# output=[]
# res=''
# for char in s:
#     if char != ' ':
#         res += char
#     elif char == ' ':
#         output += [res]
#         res=''
# output += [res]
# print(output)

# s='the quick brown fox'
# ls=s.split()
# total=0
# res=''
# for i in ls:
#     if len(i)>total:
#         total=len(i)
#         res=i
# print(res)


# s='dfedfghijk'
# out=''
# for i in range(len(s)):
#     temp=s[i]
#     for j in range(i+1,len(s)):
#         if s[j] not in temp:
#             temp += s[j]
#         else:
#             if len(out)< len(temp):
#                 out=temp
#             break
#     else:
#         if len(out)<len(temp):
#             out=temp
# print(out)

# s = 'adobecodebanc'
# w = "abc"
# out=s
# # l1=[]
# for i in range(len(s)):
#     temp=s[i]
#     for j in range(i+1,len(s)):
#         temp +=s[j]
#         if len(temp) >= len(w):
#             c=0
#             for ele in w:
#                 if ele in temp:
#                     c+=1
#             else:
#                 if c==3:
#                     if len(out) >= len(temp):
#                         out=temp
#                     # l1.append(temp)
# print(out)


# def fun_name(name):
#     for each in name:
#         return (f"my name ,{each}!")
# print(fun_name('hello'))

'''add two numbers'''
# m=lambda a,b : a + b
# print(m(1,3))

'''square number'''
# sq=lambda x : x * x
# print(sq(5))

'''Check Even or Odd'''
# num = lambda x : 'even'  if x%2==0 else 'odd'
# print(num(int(input('enter number : '))))

'''list inside element even or odd'''
# ls=[2,4,7,5,6]
# even = list(filter(lambda x : x%2 ==0 ,ls))
# odd = list(filter(lambda x : x%2!=0,ls))
#
# print('even numbers : ',even)
# print('odd numbers  : ', odd)


''' Sort List of Tuples by Second Value'''
ls = [(1,3),(1,2),(2,2)]

'''armstrong'''
# def arm_str(num,res):
#     l=len(str(num))
#     dup=num
#     while num>0:
#         digit = num%10
#         res += digit**l
#         num//=10
#
#     if res == dup:
#         return 'Armstrong'
#     return 'not Armstrong'
#
# num=int(input('enter number : '))
# res=0
# print(arm_str(num,res))

'''palindrome string'''
# def pali_str(s):
#     res=''
#     for char in s:
#         res = char + res
#     return res
# print(pali_str(input('enter string : ')))


# ls=['amma','hello' ,'ini','super']

# def pali_lst(ls):
#     emp=[]
#     for each in ls:
#         res=''
#         for char in each:
#             res = char + res
#         if each == res:
#             emp.append(res)
#     return emp
# ls=['amma','hello' ,'ini','super']
# print(pali_lst(ls))


# def pali_str(ls):
#     emp=[]
#     for each in ls:
#         if each == each[::-1]:
#             emp.append(each)
#     return emp
# ls=['amma','hello' ,'ini','super']
# print(pali_str(ls))

# def prime_ls(ls):
#     emp=[]
#     for each in ls:
#         count = 0
#         for ele in range(1,each+1):
#             if each%ele ==0:
#                 count+=1
#         if count == 2:
#             emp.append(each)
#     return emp
#
# ls=[23,2,51,73,6,56]
# print(prime_ls(ls))

# def coprime_ls(ls):
#     emp=[]
#     for each in ls:
#         count=0
#         for ele in range(1,each+1):
#             if each%ele==0:
#                 count +=1
#
#         if count >2:
#             emp.append(each)
#     return emp
#
# ls=[2,15,3,67,45,7,8]
# print(coprime_ls(ls))

'''prime number'''
# def fun_prime(num):
#     count=0
#     for ele in range(1,num+1):
#         if num%ele == 0:
#             count+=1
#     if count==2:
#         return 'prime'
#     return 'not prime'
# print(fun_prime((8)))

def fact_num(num):
    fact = 1
    if num !=0:
        fact = num * fact_num(num -1)
    return fact
print(fact_num(5))










