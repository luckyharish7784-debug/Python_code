# s=input('enter string : ')
# d={}
# for i in s:
#     if i not in d:
#         d[i] =1
#     else:
#         d[i] = d[i]+1
# print(d)
        

# s= {'listen':'silent'}

# d1= {'a':1}
# d2={'b':2}
# d1.update(d2)
# print(d1)

# d1={'a':1,'b':2}
# d2={'b':3,'c':4}
# res=[]
# for key in d2:
#     if key not in d1:
#        res.append(key)

# for key1 in d1:
#     if key1 not in d2:
#         res.append(key1)

# print(set(list(res)))

# d={'a':(1,2),'b':(2,3),'c':(1,2)}
d1= input('enter dict : ')
value = list(d1.values())
d=value[0]
res=()
for i in range(1,len(value)):
    if value[i] == d:
        res += value[i]
print(res)
        


