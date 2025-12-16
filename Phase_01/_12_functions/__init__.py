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














