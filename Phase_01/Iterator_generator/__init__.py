# Are you use in realtime in iterator (No)
'''
In realtime we can use only Generator (Large amount data) and iterator(Small amount data)
Iterator and generator:
Iterator: sequence of items
1.It is an object which contain sequence of items which u can fetch only specific order.

Generator:
1.It is a type of iterator and all generator are iterator
2.by default in iter and next
3.

Iterable: which have unpacking capacity

__iter__ (To fetch the data)
__next__(rem the current position and return the next value or element and after the completed the elements it throws
             error STOP ITERATION)


iterator =['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
          '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__',
           '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__',
            '__sizeof__', '__str__', '__subclasshook__']

Process

'''




# ls=[1,2,3,4,5,6]
# print(id(ls))
# new_ls = iter(ls)
# print(id(new_ls))
# print(new_ls)
# print(dir(new_ls))


# ls = [10,20,30]
# new=iter(ls)

# print(new.__next__())
# print(new.__next__())
# print(new.__next__())
# print(new.__next__())

# print(new.__iter__())
# print(new.__iter__())
# print(new.__iter__())
# print(new.__iter__())

# class RangeIterator:
#
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         new = self.start
#         if self.start >= self.stop:
#             raise StopIteration
#         self.start += 1
#         return new
#
#
# obj = RangeIterator(1,5)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
'''==========================================================================='''
# class Squarenumber:

#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         total = self.start * self.start
#         if self.start >= self.stop:
#             raise StopIteration
#         self.start  += 1
#         return total
# obj = Squarenumber(1,5)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

'''===================================================================================='''

'''Implement a generator function that yields Fibonacci numbers'''
# class Fib_num:
#     def __init__(self,start,stop):
#         self.start =start
#         self.stop =stop
#         self.a =0
#         self.b=1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
        
#         total_value =self.a
#         self.a,self.b =self.b , self.a + self.b
#         self.start +=1
#         return total_value
    
# obj = Fib_num(0,5)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

'''==================================================================================='''

# s='hello,world'
# res=''
# for i in s:
#     if i != ',':
#         res += i
#     elif i == ',':
#         res +=' '
        
# print(res)

'''========================================================================================'''
# class fib_num:
#     def __init__(self,start,stop):
#         self.start =start
#         self.stop =stop
#         self.a =0
#         self.b = 1
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         total_value = self.a
#         self.a,self.b = self.b,self.a+self.b
#         self.a += 1
#         return total_value
    
# obj = fib_num(1,7)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# ==========================================================================

# def fib(num):
#     first,second = 0,1
#     for i in range(0,num):
#         yield first
#         first,second = second,first+second
# res = fib(int(input('enter number : ')))
# try:
#     while True:
#         print(next(res))
# except StopIteration:
#     print('completed....')


# num = eval(input('enter a list : '))
# empt=num[0]
# for i in num:
#     if i > empt :
#         empt = i
# print(f'largest number is {empt}')
        

# n = int(input("Enter number of elements: "))

# nums = []
# for i in range(n):
#     val = int(input(f"Enter element {i+1}: "))
#     nums.append(val)

# largest = nums[0]   # assume first element is largest

# for num in nums:
#     if num > largest:
#         largest = num

# print("Largest number:", largest)


# a = {'a':1,'b':2}
# b=a
# a = a.update(["c3"])
# print(a,b)

# d={'a':1,'b':2,'d':3}
# m=d.get('n')
# print(m)

# d={'a':10,'b':[10,20],'c':{'a':10,'b':20}}
# total =0
# for value in d.values():
#     if isinstance(value,int):
#         total += value
        
#     elif isinstance(value,dict):
#         res=0
#         for i in value.values():
#             res += i
#         total += res /len(value)
    
#     elif isinstance(value,list):
#         res1 =0
#         for i in value:
#             res1+=i
#         total +=res1/len(value)
       

# average = total/2
# print(average)

# d1={}
# for key in d.keys():
#     d1[key]=average
# print(d1)



# l=[1,2,3,[4,5,[6,7,[8,9]]]]
# import csv
# with open('file.csv','r',newline='') as e:
#     l=e.read()
#     ls=list(l)
# lt=ls
# m=[]
# for each in lt:
#     if type(each) == list:
#         lt += each
#     else:
#         m.append(each)
# print(m)

# a=int("21",2)
# # b=int(a)
# print(a)

# cart =("shoe","bag","watch")
# a,b,c = cart
# print(b)
# s={1,2,3,2,3,4,5,3,4,8}
# print(s)

# import csv
# l=[1,2,3,[4,5,[6,7,[8,9]]]]
# with open('file.csv','w') as e:
#     write=csv.write(e)
#     write.writerow(l)
# print('csv file inserted successfully')

