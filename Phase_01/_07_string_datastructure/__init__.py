'''
string:
immutable
sequence
ordered
iterable
'' "" ''' '''  """ """
1114112
builtin methods -47

builtin methods:
lower upper title capitalize swapcase casefold  - 6
count index rindex find rfind format format_map - 7
islower isupper istitle isalpha isalnum isascii isdigit isnumeric isdecimal isidentifier isprintable isspace - 12
center zfill ljust rjust - 4 
strip lstrip rstrip  - 3
split rsplit splitlines - 3
startswith endswith removesuffix removeprefix paritition rpartition  - 6
join replace maketrans translate expandtabs encode - 6




'''



# s='hello'
# s1='world'
# s3='to all'
# f=s1+s3+s
# print(f)














#max
# my_str = 'python good'
# org_str = max(my_str)
# print(org_str)

# my_str = 'hello world!'
# org_str = min(my_str)
# print(org_str)
# print(ord(' '))

#Reverse the given string
s='hello'
''' 
hello
01234
output:olleh
'''
# print(s[::-1])
# print(len(s)-1::-1)

# ---------------------------------------------------------------------------------
'''Problem: Check if a string is a palindrome.
s='racecar'
racecar
0123456
output : True

'''
# s='racecar'
# emp = s[::-1]
# if s == emp:
#     print(True,'It is a palindrome')
# else :
#     print(False,'it is not palindrome')

#==============================================================================

'''
count vowels
Problem: Count the number of vowels in a string.

s='apple'
vowels = a,e,i,o,u
'''
# s= 'apple'
# count = 0
# vowels_str = 'a,e,i,o,u,A,E,I,O,U'
# for each in s:
#     if each in vowels_str:
#         count = count+1
# print(count)
# s='apple'
# count=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         count+=1
# print(count)
# ==================================================================================

'''
To Uppercase Problem: Convert a string to uppercase. 
Input: "hello" 
Expected Output: "HELLO"

print(ord('h')) -- value- 104
print(chr(97)) -- character 'a' --- to converted integer to string

'''
s = 'hello'
emp =''
n1 = ''
n2 = 90
for each in s:
    emp =emp+ chr(ord(each) - 32)
print(emp)

# ==============================================================================================

'''
To Lowercase Problem: Convert a string to lowercase. 
Input: "HELLO" 
Expected Output: "hello"

print(ord('H'))  --- 
print(chr(104))
'''
# s = 'HELLO'
# res = ''
# for each in s:
#     res = res + chr(ord(each)+32)
# print(res)
# ====+===============================================================
# s = 'python'
# x=s.upper()
# print(x)
#
# s='PYTHON programming is very easy'
# print(s.lower())
# print(s.title())
# print(s.capitalize())

# print(s.swapcase())
# print(s.casefold())
# x=s.count('z')
# print(x)
# x=s.index('l')
# print(x)
# x=s.find('a')
# print(x)
# n=s.rfind('a')
# print(n)

# ============================================================================
# s='success depends on the second letter'
# print(s[-9:0:-1])


# # print(s[-1::-1])
# s=input('enter name : ')
# res = ''
# for each in s:
#     if each not in res:
#         res = res + each
# print(res)
# print(s)
'''
builtin methods
lower upper title capitalize swapcase casefold
count index rindex find rfind format format_map
islower isupper istitle isalpha isalnum isascii isdigit isnumeric isdecimal isidentifiers is
'''
# s=' h e l l o '
# # #o/p:'hello'
# x=s.replace(' ','')
# print(x)

'''Count pairs of words that form palindrome when concatenated. 
Input: ["bat", "tab", "cat"]
Expected Output: 1'''
# inp=["bat","tab","cat"]
# count=0
# for ele in range(len(inp)):
#     for ele1 in range(len(inp)):
#         if inp[ele] != inp[ele1]:
#             out=inp[ele]+inp[ele1]
#             if s== s[::-1]:
#                 count+=1
# print(count)

'''
Smallest Window Containing Subsequence 
Problem: Find smallest substring containing given subsequence.
 Input: "abcdebdde", "bde" 
 Expected Output: "bcde"'''


'''Factorial number by using while loop'''

# num=int(input('enter number : '))
# fact =1
# while num > 0:
#     fact = fact * num
#     num -=1
# print(fact)

'''Given number is prime or not'''
# num=int(input('enter number : '))
# count=0
# if num!=1:
#     for ele in range(2,num+1):
#         if num%ele ==0:
#             count+=1
#
#     if count==1:
#         print('it is a prime number')
#     else:
#         print('it is not prime number')
# else:
#     print('it is not prime number')

# ls=[[1,2,3],[2,3,4],[3,4,5]]
# #output=[3]
# emp=[]
# total =len(ls)
# for ele in ls[0]:
#     c=0
#     for ele_1 in ls:
#         if ele in ele_1:
#             c+=1
#     if c== total:
#         emp.append(ele)
# print(emp)

'''Given string is palindrome or not'''
# s= input('enter string : ')
# duplicate = s
# res=''
# i=len(duplicate)-1
# while i >=0: #while i>-1:
#     res += duplicate[i]
#     i -=1
# if res==s:
#     print('it is palindrome ')
# else:
#     print('it is not palindrome')


#=====================================================================
# s = input("Enter a string: ") #hello
#
# output=''
# for char in s:
#     if char not in output:
#         count=0
#         for ele in s:
#             if char == ele:
#                 count+=1
#         print(char ,':',count,end=' ')
#         output += char

# d1={'a':10,'b':20,'c':[10,20,30]}
# d1.get(10)
# value_d = d1.get('d')
# print(d1)
# print("Value for 'a':", value_d)
# ls=[]
# ls.pop(1)
# print(ls)

