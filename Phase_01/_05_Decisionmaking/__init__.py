'''
decision_making :

if elif else



'''
# Task: Take the length and breadth of a rectangle as input from the user and find whether it is a square or not.

# length = float(input('enter length value :'))
# breadth = float((input('enter breadth value :')))
#
# if length == breadth :
#     print('It is square')
# else:
#     print('it is not square')
# --------------------------------------------------------------------------------
# Take a single character as input from the user and find whether it is uppercase or lowercase.

# char_type = input('enter character : ')
# if char_type == char_type.upper():
#     print('character is uppercase')
# elif char_type == char_type.lower():
#     print('character is lowercase')
# else :
#     print('character is not uppercase or lowercase')

# char_type = input('enter character : ')
# if len(char_type) == 1:
#     if 'a' <= char_type <= 'z':
#         print('lower character')
#     elif 'A' <= char_type <= 'Z':
#         print('Upper character')
#     else:
#         print('enter valid input character ')
# else:
#     print('enter only one character ')

# s_a_char = input('enter single alpha character : ')
# l_char = 'a,e,i,o,u,A,E,I,O,U'
# if s_a_char in l_char:
#     print('vowels character')
# elif s_a_char not in l_char:
#     print('consonant character')
# else:
#     print('only single alpha character')
#
# weekday from number

# week = int(input('enter number 1 to 7 : '))
#
# if week == 1 :
#     print('Monday')
# elif week == 2:
#     print('tuesday')
# elif week == 3 :
#     print('wednesday')
# elif week == 4 :
#     print('thursday')
# elif week  ==5 :
#     print('friday')
# elif week == 6 :
#     print('saturday')
# elif week == 7 :
#     print('sunday')
# else:
#     print('enter valid number from 1 to 7')

# cube from number
# num = int(input('enter a number : '))
# print(num ** 3)

# print(ord('a'))

#Take a number n as input from the user and find the sum of first n odd natural numbers.
# num=int(input('enter number : '))
# sum_num = 0
# odd = 1
#
# for i in range(num):
#     sum_num = sum_num + odd
#     odd = odd + 2
# print('sum of first ',num,'odd natural number ', sum_num)

#Take an integer as input from the user and find the cube of all numbers up to that integer.
#
# num = int(input('enter number : '))
# start = 1
# pow =0
# while num >= start:
#     pow = start ** 3
#     start = start+1
#     print(pow)


# num = int(input('enter number : '))
# pow =0
# for start in range(1,num+1):
#     pow = start **3
#     print(pow)

#Take three numbers as input from the user and find whether they are in increasing, decreasing, or neither order

# num = int(input('enter number : '))
# num_1 = int(input('enter number : '))
# num_2 = int(input('enter number : '))
#
# if num < num_1 < num_2:
#     print('increasing the number')
# elif num > num_1 > num_2:
#     print('decreasing the number')
# else:
#     print('neither ascending or descending order')

#Take three names as input from the user and find their order in descending alphabetical order.

# char = input('enter character : ')
# char_1 = input('enter character : ')
# char_2 = input('enter character : ')
#
#
# if char > char_1 > char_2:
#     print('decreasing character')
# else:
#     print(' ascending character')

#===============================================================

# Match case statement
# num=int(input('enter a day : '))
# match num:
#     case 1:
#         print('monday')
#     case 2:
#         print('tuesday')
#     case 3:
#         print('wednesday')
#     case 4 :
#         print('thursday')
#     case 5:
#         print('friday')
#     case 6:
#         print('saturday')
#     case 7:
#         print('sunday')
#     case _:
#         print('enter week days name only ')

#===========================================================================

'''weekday from number
Task: Take a number between 1 to 7 as input from the user and 
find the corresponding weekday name.'''
# num = int(input('enter weekday number : '))
# match num:
#     case 1:
#         print('Today is Monday')
#     case 2:
#         print('Today is Tuesday')
#     case 3:
#         print('Today is Wednesday')
#     case 4:
#         print('Today is Thursday')
#     case 5:
#         print('Today is Friday')
#     case 6:
#         print('Today is Saturday')
#     case 7:
#         print('Today is Sunday')
#     case _ :
#         print('enter valid number')

#=====================================================================

''' Pattern program'''
# num=int(input('enter number: '))
# minus=num-1
# for i in range(1,num+1):
#     print((' '*minus),'*'*i)
#     minus -=1

#==================================================================

'''
Leap Year Checker • Task:
Take a year as input from the user and 
find whether it is a leap year or not.'''
# year =int(input('enter year number : '))
# if (year%4==0 and year%100==0) or year%400 ==0:
#     print('leap year')
# elif (year%4!=0 and year%100==0):
#     print('non  leap year')
# else:
#     print('enter four digit year number')

# year = int(input('enter year number : '))
# if year%400==0:
#     if year%100!=0 and year%4==0:
#         print('leap year')
#     else:
#         print('non leap year')
# else:
#     print('non leap year')

#====================================================================

'''Find the Largest of Three Numbers • Task: 
Take three numbers as input from the user and find the largest number.
'''

# num=int(input('enter number : '))
# num_1 = int(input('enter number_1 : ' ))
# num_2 = int(input('enter number_2 : '))
# if num > num_1 and num>num_2:
#     print(num,'largest number')
# elif num_1>num and num_1 > num_2:
#     print(num_1,'largest number_1 ')
# else:
#     print(num,'largest number compare to num,num_1')


# print(2<1) ---false
# print(0<1) --true
# print(0>1) ---false
# print(2>1) --- true

#=================================================================================

'''Telephone Bill Calculator • 
Task: Take number of calls made as input from the user and 
find the total telephone bill.'''

# num= int(input('enter number : '))
# bill=0
# if num <=100 :
#     bill=0
# elif num <=200:
#     bill = (num-100) * 1
# else:
#     bill=(100*1)+(num-200)*2
# print('Total telephone bill ', bill)

#=============================================================================================

'''Even or Odd Number Checker • Task: 
Take a number as input from the user and find whether it is even or odd.
'''
# num=int(input('enter number : '))
# if num%2==0:
#     print('even number is : ',num)
# else:
#     print('odd number is : ',num)

#===============================================================================

'''Exam Eligibility Based on Attendance • 
Task: Take number of classes held and number of classes
 attended as input from the user and find the attendance percentage and 
whether the student is allowed to sit in the exam.
'''
# total_classes= int(input('enter total classes : '))
# present_class=int(input('enter number of classes : '))
#
# percentage_attendance = (present_class / total_classes)* 100
# print('present of percentage attendance : ',percentage_attendance)
#
# if (percentage_attendance >=75):
#     print('eligible for the exam ')
# else:
#     print('Not eligible for the exam ')

# #===============================================================================
#
'''ARMSTRONG NUMBER'''
# num = int(input('enter armstrong number : '))
# dupl=num
# dum = 0
#
# while dupl >0:
#     dupl //= 10
#     dum += 1
# dupl = num
# res=0
#
# while dupl >0:
#     digit = dupl%10
#     res = res + (digit ** dum)
#     dupl //=10
#
# if num == res :
#     print('armstrong number')
# else:
#     print('not armstrong number')

#========================================================
'''
STRONG NUMBER
145== 1(factorial) +4(factorial)+5(factorial)
'''
# num =int(input('enter number : '))
# dup_num = num
# res=0
# while dup_num > 0:
#     digit = dup_num%10
#     fact = 1
#     for i in range(1,digit+1):
#         fact = fact * i
#     res += fact
#     dup_num//=10
#
# if num == res:
#     print('strong number',num)
# else:
#     print('non strong number',num)

#=================================================================
'''
palindrome number
121=121 (input a reverse also same number)
 132=231
 '''
# num =int(input('enter number : '))
# temp = num
# res=0
# while temp >0:
#     digit = temp %10
#     res =res*10+digit
#     temp = temp//10
#
# if res == num:
#     print('palindrome number ',num)
# else:
#     print('not palindrome number',num)





