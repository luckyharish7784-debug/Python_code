'''Dict to List of Tuples
Problem: Convert dictionary to list of (key, value).
Input: {'x':1, 'y':2}
Expected Output: [('x',1), ('y',2)]'''
# d={'x':1,'y':2}
# output=[]
# for key in d:
#     if key not in output:
#         output= output +  [(key,d[key])]
# print(output)


# s='hello'
# output={}
# for ele in s:
#     if ele not in output:
#         output[ele]=1
#     else:
#         output[ele]+=1
# # print(output)
#
# ls=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
#
# #output=[[7,4,1],[8,5,2],[9,6,3]]
# output=[]
# for ele in ls:
#     empty=[]
#     for ele_1 in range(len(ele)):
#         empty.append(ls[ele_1][ele])
#     else:
#         output.append(empty[::-1])
# print(output)

#
# ls=[[1,2,3],
#     [4,5,6],
#     [7,8,9]]
# res=[]       # Create empty list in global declaration
# for i in ls:
#     output= [] # create one more empty list in global declaration
#     for j in range(len(i)):
#         output.append(ls[j][i])
#     else:
#         res.append(output[::-1])
# print(res)

# s='abcdcddeec'
# out=''
# emp=''
# count=0
# for i in s:
#     if i not in emp:
#         count = 1
#         emp = emp + (i + ':' + str(count) + ' ')
#     else:
#         count +=1
#         emp = emp + (i + ':' + str(count) + ' ')
# print(emp)


# ls=[11,29,18,4,7,2]
# for i in range(0,len(ls)-1):   #(0,5)
#     for j in range(0,len(ls)-i-1): #(0,5)
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]
# print(ls)
# ===============================================================

# old1 = {'x':{'a':1,'b':3,'x':4},'b':65,'c':45}
# new1 = {'y':2,'f':{'x':4},'m':32}
def swap_dict(old1):
    d={}
    for key,value in old1.items():
        if isinstance(value,dict):
            d[key]=swap_dict(value)
        else:
            d[value]=key
    return d
old1 = {'x':{'a':1,'b':3,'x':4},'b':65,'c':45}
# new1=swap_dict(old1)
print(swap_dict(old1))

















