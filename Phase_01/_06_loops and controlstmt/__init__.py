'''

req :
state:state is nothing but datatype/datastructures is required to input/output
beh : behavior is nothing but Business logic ---> CURD, decision making , loops, operators.

mutable - we can create after modify or update the items or elements.
list, set, dict
immutable : we can't create after modify or update the elements
int, float, complex, boolean, str,tuple

'''
# s='developers'
#
# for i in s:
#      print(i)
#
# l= [10,20,30,50,40]
#
# for i in l:
#     print(i)
#
# x= {'a':13,'n':9,'j':8}
# # print(x['n'])
# # for i in x :
# #     print(i)

# s= {'ram','iti','surya','gani','hari','sai'}
#
# for i in s:
#     if  i == 'surya':
#         break
#     print(i)
# l='python'
# count = 0
# for i in l:
#     count += 1
#     if i == 't':
#         break
#     print(i)
# print(count)

# s=[10,30,40,60,99]
#
# for i in s:
#     pass
#     if i == 30:
#         print('hello')
#     print(i)


# print all 1 to 100 numbers

# num = 100
# for i in range(1,num+1):
#     print(i,end=' ')
#     i+=1

# num = 1
# while num <=100:
#     print(num)
#     num +=1

# print even numbers between 1 to 100

# num = 100
# for i in range(1,num+1):
#     if i%2==0 :
#         print(i)
#

# num = 1
# while num<=100:
#     if num%2==0:
#         print(num)
#     num += 1
# print odd number between 1 to 100

# num = 100
# for i in range(1,num+1):
#     if num%i != 0:
#         print(i)

# num = int(input('enter number : '))
# while num <= 100:
#     if num%2 != 0 :
#         print(num)
#     num += 1

# print all numbers between 1 to 100 from divisible by 5 and 7

# num = int(input('enter number : '))
# for i in range(1,num+1):
#     if i%5 == 0 and i%7==0:
#         print(i)
#     i += 1

# num= int(input('enter number : '))
# while num<=100:
#     if num%5==0 and num%7==0:
#         print(num)
#     num += 1

# print a factorial number between 1 and 100
# fact =int(input('enter number : '))
# res = 1
# while fact > 1:
#     res = res * fact
#     fact -= 1
# print(res)

# print all number between 1 to 100 is divisible by 4 and 6
# num = int(input('enter number : '))
# for i in range(1,num+1):
#     if i%4 == 0 and i%6==0:
#         print(i)
#     i += 1

# num = int(input('enter number : '))
# i=1
# while i <=num:
#     if i%4 == 0 and i%6 == 0:
#         print(i)
#     i += 1

# print first 14 even numbers between 1 to 100

# num = int(input('enter number : '))
# count = 0
# num_1 = int(input('enter number fetch : '))
# for i in range(1,num+1):
#     if count != num_1:
#         if i%2 == 0 :
#             count += 1
#             print(i)
#         i += 1
#
# num = int(input('enter number : '))
# count =0
# fetch_num = int(input('enter fetch number : '))
# start = 1
# while num != start:
#     if count != fetch_num :
#         if start%2 == 0:
#             count+=1
#             print(start)
#         start += 1
#     else :                      # why use else and break means (after output also still running but no output that why i'm using else and break)
#        break

# print first 24 odd numbers between 1 to 100

# num = int(input('enter number : '))
# fetch_num = int(input('enter fetch number : '))
# count = 0
# for start in range(1,num+1):
#     if count != fetch_num:
#         if start%2 != 0 :
#             count += 1
#             print(start)
#         start += 1

# num = int(input('enter number : '))
# start =1
# fetch_num = int(input('enter fetch number : '))
# count = 0
# while start <= num:
#     if count != fetch_num:
#         if start%2 != 0:
#             count +=1
#             print(start)
#         start += 1
#     else :
#         break

#print first n numbers which are divisible by 4 and 6 between 1 and 100

# num = int(input('enter number : '))
# count = 0
# fetch_num = int(input('enter first fetch number : '))
# for start in range(1,num+1):
#     if count != fetch_num :
#         if start%4 == 0  and start%6 == 0:
#             count += 1
#             print(start)
#         start = start+1


#print all numbers except divisible by 9

# num = int(input('enter number : '))
# for start in range(1,num+1):
#     if start%9 != 0:
#         print(start)
#     start +=1

# num = int(input('enter number : '))
# start = 1
# while num >= start:
#     if start%9!=0:
#         print(start)
#     start += 1

# l=[1,2,3,4]
# emp =[]
# for i in l:
#     emp.insert(0,i)
# print(emp)

# l= [1,2,3,4]
# emp =[]
# for i in range(len(l)-1,-1,-1):
#     emp.append(l[i])
# print(emp)
'''
loop:
-----
loop in python are used to repeat actions effectively.
there are 2 types of loops.
1.for loop
2.while loop

1.for loop:
-----------
for loop is used to untill sequence or finite data.

2.while loop:
--------------
while loop is used to execute a block of statements repeatedly until a given condition  is satisfied.

difference between while loop and for loop?
          for loop                                  while loop
1.uses "for" keyword                  1.uses "while" keyword
2.the for loop is faster than         2.the while loop is relatively slower than for loop
   while loop
3.The loop runs infinite times        3.Returns the compile time error in the 
  in the absence of condition.          absence of condition.
4.The for loop is to iterate,the      4.there is so such function in the while loop.
   range or xrange function is used
'''
#i want 1 to 10 numbers.
# num = 10
# for start in range(1,num+1):
#     print(start)

# # i want 20 numbers
# num=int(input('enter number : '))
# for start in range(1,num+1):
#     print(start)
# else:
#     print("enter a valid number ",num)

#how many iteration is happened
# count=0
# while count<4:
#
#     print('hello its working')
#     count += 1

# ls=[1,3,2,4,2,5,6]
#
# for i in ls:
#     print(i)

# ls=[123,456,789]
# #o/p=[321,654,987]
# empt=[]
# for each in ls:
#     num=each
#     res=0
#     while (num>0):
#         rem = num%10
#         res= res*10 + rem
#         num//=10
#     empt += [res]
# print(empt)

# num=int(input('enter number : '))#7894--9478
# res=0
# while num>0:
#     rem = num%10
#     res = res*10 + rem
#     num//=10
# print(res)

# dit={'a':10,'b':20}
# # for each in dit:
# #     print(each,dit[each])

# ls=[1,2,3]
# ls2=[5,6,7]
# res=ls+ls2
# print(res)

# xk = '10j+1@1'
# print(xk)

# for i in range(5):
#     if i==2:
#         continue
#     print(i)

# for i in range(6):
#     if i == 3:
#         break
#     print(i)

# for i in range(5):
#     if 3==i:
#         pass
#     print(i)

# x=10
# if x > 5:
#     pass
# else:
#     print('x is 5 or less')

d={'a':10,'b':20,'c':[3,5]}
d1=d
d1['c'][0]=99
print(d1)
print(d)
