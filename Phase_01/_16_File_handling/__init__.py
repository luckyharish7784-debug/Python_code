'''
File Handling

'''
# with open('file1.txt','w') as f:
#     s='this is ferilion labs'
#     f.write(s)
# #

# with open('file2.txt','r') as f:
#     print(f.read())                 #file is not present it throws "FileNotFoundError "
#

# with open('file3.txt','r+') as f:
#     print(f.read())
#     f.seek(0)
#     s='hello everyone'
#     print(f.write(s))                 #file is not present in R+ mode it throws error "FileNotfound Error"

# with open('file3.txt','w+') as f:
#     s= ('Today Topic is handling'
#         'python and mysql')
#     print(f.write(s))
#     f.seek(0)
#     print(f.readlines())

# with open('file3.txt','a+') as m:

with open('file3.txt','r+') as f:
    f.seek(0)
    print(f.read())
    s='hello everyone'
    print(f.write(s))
