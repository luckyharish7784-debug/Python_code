'''
set properties:
1.mutable
2.unordered
3.iterable
4.set(),{element,}
5.builtin methods-17

adding -add
removing - pop remove discard clear

update
'''

# s.add(5)
# print(s)

# s.clear()
# print(s)

# s.remove(7)
# print(s)

# s={1,2.4,5j}
# s.discard(5j)
# print(s)
#
# s1={1,2,3}
# s2=[2,4,5]
# # s3=s1.difference(s2)
# # s4=s1.symmetric_difference(s2)
# s5=s1.intersection(s2)
# print(s5)

# s1={1,2,3}
# s2={4,3,5,6}
# if s1.isdisjoint(s2):
#     print(True)
# else:
#     print(False)


# =========================================================
# ls=[1,2,3,4,5]
# k=2
# for each in range(k):
#     last = ls[-1]
#     for each_1 in range(len(ls)-1,0,-1):
#         ls[each_1] = ls[each_1-1]
#     ls[0]=last
# print(ls)



# ls=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last = ls[-1]
#     for j in range(len(ls)-1,0,-1):
#         ls[j]= ls[j-1]
#     ls[0]=last
# print(ls)
# ======================================================
# ls=[1,2,3,4,5]
# k=2
# for i in range(k):
#     last = ls[-1]
#     for j in range(len(ls)-1,0,-1):
#         ls[j]= ls[j-1]
#     ls[0]=last
# print(ls)

# ls=[1,2,3,4,5]
# k=2
# output_ls = []
# res=[]
# emp=[]
# for i in ls:
#     if i>(k+1):
#         res += [i]
#     elif i<=(k+1):
#         emp += [i]
# output_ls = output_ls+res+emp
# print(output_ls)


ls=[3,1,2,3,2]
# #output = [3,1,2]
# empt=[]
# for each in ls:
#     if each not in empt:
#         empt += [each]
# print(empt)


# empt=[]
# for each in ls:
#     if each not in empt:
#         empt.append(each)
# print(empt)

# ========================================================

# Find a continuous sublist that sums to target.
# Input: [1, 2, 3, 4, 5],
# target=9 Expected Output: [2, 3, 4]

# ls=[1,2,3,4,5]
# target = 9
# res=[]
# for start in range(len(ls)):
#     for each in range(start+1,len(ls)):
#         for e_ch in range(each+1,len(ls)):
#             if target == ls[start]+ls[each]+ls[e_ch]:
#                 res = [ls[start],ls[each],ls[e_ch]]
# print(res)

#=============================================================

# Find the longest streak of 1s in binary list.
# Input: [1,1,0,1,1,1] Expected Output: 3

# ls=[1,1,0,1,1,1,1,1]
# count = 0
# max_len = 0
# for each in ls:
#     if each == 1:
#         max_len += 1
#     else :
#         count = max(max_len,count)
#         max_len=0
# count = max(max_len,count)
# print(count)
# # print(max(max_len,count))

#=============================================================================

# Return list intersection of two lists.
# Input: [1, 2, 3], [2, 3, 4] Expected Output: [2, 3]

# ls1=[1,2,3]
# ls2=[2,3,4]
# res=[]
# for i in ls1:
#     if i in ls2:
#         res += [i]
# print(res)

# ls1=[1,2,3]
# ls2=[2,3,4]
# res=[]
# for each in ls1:
#     if each in ls2:
#         res.append(each)
# print(res)

#=====================================================================

# Find missing number from list of 1 to n.
# Input: [1, 2, 4, 5] with n=5 Expected Output: 3

# list_1=[1,2,4,5]
# num=5
# res=0
# # for start in range(num):
# for start in range(1,num):
#     if start not in list_1:
#         res += start
# print(res)

#
# list_s=[1,2,4,5]
# num=5
# res=0
# for start in range(1,num):                          doubt code
#     if start not in list_s:
#         res.append(start)
# print(res)

#=================================================================================

# Find missing number from list of 1 to n.
# Input: [1, 2, 4, 5] with n=5 Expected Output: [0,3,7]

# list_1=[1,2,4,5,7]
# total=7
# res=[]
# for each in range(total):
#     if each not in list_1:
#         res += [each]
# print(res)

# ==========================================================================

# Find median of two sorted lists.
# Input: [1, 3], [2] Expected Output: 2
# Example 2: Input: [1, 2], [3, 4] Expected Output: 2.5




# Problem: Move zeros to end preserving order.
# Input: [0, 1, 0, 3, 12] Expected Output: [1, 3, 12, 0, 0]

# lts_1 = [0,1,0,3,12]
# num = int(input('enter which number : '))
# res=[]
# empt=[]
# for each in lts_1:
#     if each == num:
#         res += [each]
#     else:
#         empt +=[each]
# empt = empt + res
# print(empt)


# lts_1 = [0,1,0,3,12]
# # zero=lts_1.count(0)
# # for each in range(zero): or number provide
# for each in range(len(lts_1)):
#     lts_1.remove(0)
#     lts_1.append(0)
# print(lts_1)

# =================================================================================
# s={1,4,100,3,2}
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())

#=============================================================================
# ls=123
# res=0
# while(ls!=0):
#     ele = ls%10
#     res = (res*10)+ele
#     ls//=10
# print(res)

#========================================================================
# l1=[10,2,10,4,5,10,8,10,6,7,10,11,10]
# #output = [10,2,4,5,10,8,100,6,7,300,11,10]
#
# for ele in range(1,len(l1)-1):
#     if l1[ele]==10:
#         if l1[ele+1]%2==0 and l1[ele-1]%2==0:
#             l1[ele]=100
#         elif l1[ele+1]%2!=0 and l1[ele-1]%2!=0:
#             l1[ele]=300
#         else:
#             l1[ele]=10
# print(l1)
#
# # ls=[1,2,2,3,4,3,2,1,2]

#===========================================================================================

# user_input = input('enter string : ')
# count_char={}
# for ele in user_input:
#     if ele not in count_char:
#         count_char[ele]=1
#     else:
#         count_char[ele] += 1
# print(count_char)

#==============================================================================================
'''check anagram'''
#
# inp_dict={'listen':1}
#
# key_1=list(inp_dict.keys())[0]
# value_1 = list(inp_dict.values())[0]
#
# key_1=key_1.lower()
# value_1=value_1.lower()
#
# if len(key_1)==len(value_1):
#     count={}
#     count1={}
#     for ele in key_1:
#         if ele not in count:
#             count[ele]=1
#         else:
#             count += 1
#     for ele in value_1:
#         if ele in count1:
#             count1[ele] += 1
#         else:
#             count1[ele]=1
#     print(count==count1)
# else:
#     print(False)




# x=['bat', 'tab', 'cat']
# # Expected Output: {'abt':['bat','tab'], 'act':['cat']}
# ls=[]
# for i in x:
#     ls.append("".join(sorted(i)))
# l=list(set(ls))
# dc={}
# for i in x:
#     for j in l:
#         if j=="".join(sorted(i)):
#             if j not in dc:
#                 dc[j]=[i]
#             else:
#                 dc[j].append(i)
# print(dc)
# =================================================================================================

# d1={'a':1,'c':'jii'}
# d2={'b':2}
# # d1.update(d2)
# # print(d1)
# d={}
# for  j in d1:
#     d[j] = d1[j]
# for i in d2:
#     d[i]=d2[i]
# print(d)

#===========================================================
# l=['a','b']
# l1=[1,2]
# #excepted output = {'a':1,'b':2}
# d={}
# for i in range(len(l)):
#     d[l[i]]=l1[i]
# print(d)

#===================================================================
'''Armstrong number'''

# num= int(input('enter a number : '))
# dup=num
# count=0
# while dup >0:
#     dup//=10
#     count+=1
#
# new=num
# res=0
# while new > 0:
#     digit=new%10
#     res= res+digit**count
#     new //= 10
#
# if res == num:
#     print('It is armstrong number')
# else:
#     print('It is not armstrong number')


# ls=[153,123,1634,370,407]
# empt=[]
# for ele in ls:
#     num=ele
#     count=0
#     while num>0:
#         num//=10
#         count+=1
#
#     dup=ele
#     res=0
#     while dup >0:
#         digit=dup%10
#         res+= digit**count
#         dup//=10
#     if ele == res:
#         empt.append(res)
# print(empt)

# ls=[[1,2,3],[2,3,4],[3,4,5]]
# common=set(ls[0])
# for ele in ls[1:]:
#     common=common.intersection(ele)
# res=list(common)
# print(res)

"""Given number is strong number or not"""
# num=int(input('enter number : '))
# dup = num
# res=0
# while dup>0:
#     digit= dup%10
#     fact=1
#     while digit >0:
#         fact = fact* digit
#         digit-=1
#     res =res+fact
#     dup//=10
# if num == res:
#     print('It is a strong number')
# else:
#     print('It is not strong number')


'''given a list what are strong numbers to print in one list'''
# ls=[2,340,145,789,40585]
# emp = []
# for ele in ls:
#     dup=ele
#     res=0
#     while dup>0:
#         digit = dup%10
#         fact=1
#         while digit>0:
#             fact = fact*digit
#             digit-=1
#         res += fact
#         dup//=10
#     if ele == res:
#         emp.append(res)
# print(emp)


# ls=[2,5,3,6]
# emp=[]
# for ele in ls:
#     fact=1
#     while ele>0:
#         fact = fact * ele
#         ele -=1
#     emp.append(fact)
# print(emp)

# ls=[[1,2,3],[2,3,4],[3,4,5]]
# common=set(ls[0])
# for ele in ls[1:]:
#     common =common.intersection(ele)
# res=list(common)
# print(res)

'''Given number is a palindrome number or not '''
# num=int(input('enter number : '))
# dup=num
# res=0
# while num>0:
#     digit=num%10
#     res=res*10+digit
#     num//=10
# if res==dup:
#     print('palindrome number')
# else:
#     print('not palindrome number')

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

# d={'a':10,'b':20,'c':30,'d':10}

"""output={}
for value in d:
    if d[value] not in [output[value]  for value in output]:
        output[value] = d[value]

print(output)"""




# ls=[123,121,541,131,1001]
# for num in ls:
#   digit = 0
#   dup = num
#   while digit < 0:
#     m = digit % 10
#     digit = digit * m + ls
#     num = num//10
#   if digit == dup:
#     print(dup, "palindrome")
# else:
#     print(dup, "palindrome number")


# num = int(input("enter the number:"))
# digit = 0
# dup = num
# while num > 0:
#     m = num % 10
#     digit = digit * 10 + m
#     num = num//10
# if digit == dup :
#    print("palindrome")
# else:
#     print("palindrome number")

# s='the quick brown fox'
# #output=['the','quick','brown','fox']
# res=''
# empty=[]
# for char in s:
#     if char != ' ':
#         res += char
#     if char == ' ':
#         empty+=[res]
#         res =''
# empty += [res]
# print(empty)

# def fact_fun(num):
#     if num==0:
#         return 1
#     else:
#         return num *fact_fun(num-1)
#
# print(fact_fun(int(input('enter number : '))))

# ls=[[1,2,3],[4,5,[6]],7,[8,9]]
# emp=[]
# for ele in ls:



# '''online shopping '''
# from abc import ABC,abstractmethod
# class Item:
#     def __init__(self,name,price):
#         self.name =name
#         self.price = price

#     def get_price(self):
#         return self.price

# class Discount(ABC):
#     @abstractmethod
#     def apply_discount(self,total):
#         pass

# class Per_discount(Discount):
#     def __init__(self,percentage):
#         self.percentage=percentage

#     def apply_discount(self,total):
#         total_bal = total * (self.percentage / 100)
#         return total_bal
# class Fix_discount(Discount):
#     def __init__(self,amount):
#         self.amount = amount

#     def apply_discount(self,total):
#         return max(0,total - self.amount)

# class Cart:
#     def __init__(self):
#         self.items = []
#         self.discount =None

#     def add_item(self,item):
#         self.items.append(item)

#     def set_discount(self,discount):
#         self.discount = discount

#     def calculate_total(self):
#         new_bal = sum(each.get_price() for each in self.items)

#         if self.discount:
#             final_bal = self.discount.apply_discount(new_bal)
#         else:
#             final_bal = new_bal
#         return final_bal

# laptop = Item('laptop',30000)
# phone = Item('phone',25000)
# my_cart = Cart()

# my_cart.add_item(laptop)
# my_cart.add_item(phone)

# my_thinking = Per_discount(10)
# my_cart.set_discount(my_thinking)
# print(f'${my_cart.calculate_total():.2f}')

# my_fix = Fix_discount(100)
# my_cart.set_discount(my_fix)
# print(f'${my_cart.calculate_total():.2f}')



s=input('enter string : ')
res=''
output=s
for i in range(len(s)):
    res = s[i]+res
if s == res:
    print('palin')
else:
    print('not palin')

























