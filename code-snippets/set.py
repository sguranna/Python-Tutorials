""" creating a set using user input"""
a=set()

n = int(input("number of elements"))
for x in range(n):
    temp = eval(input("enter the elements"))
    print(type(temp))
    a.add(temp)

print(a)
