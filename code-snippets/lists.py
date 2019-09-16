""" Program for adding two matrices"""
# a=[[10,20,30],[40,50,60]]
# b =[[11,21,31],[41,51,61]]
# res = []

# for x in range(len(a)):
#     dummy = []
#     for y in range(len(a[0])):
#         dummy.append(a[x][y]+b[x][y])
#     res.append(dummy)
# print(res)

""" Program to find the two numbers whose sum will be equal to given number"""
# a=[12,23,43,34,54,23]
# n=35
# status = False
# for x in range(0,len(a)):
#     for y in range(x+1,len(a)):
#         if(a[x]+a[y]==n):
#             print(a[x], a[y])
#             status = True
#             break
#     if(status==True):
#         break


""" programming for creating matrix using lists"""
# 4x3 matrix
m = eval(input("Enter number of rows"))
n = eval(input("Enter number of cols"))
matrix = []
for x in range(m):
    l=[]
    #n=eval(input("How many elements"))
    for x in range(n):
        a=eval(input("Enter the element"))
        l.append(a)
    matrix.append(l)
    print(matrix)

for x in matrix:
    for y in x:
        print(y)

        


