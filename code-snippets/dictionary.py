""" Creating a dictionary from user input"""
# a={}
# n = int(input("Enter the number of elements"))
# for x in range(n):
#     key = eval(input("Enter the key"))
#     value = eval(input("enter the value"))
#     a[key] = value
#     print(a)

# Accessing the elements
a={'name': 'shiva', 'age': 25, 'sal': 30000}
# for x in a:
#     print(x,a[x]) # a[key]
for x in a.values():
    print(x)

# Accessing the elements of a set
# a={10,20,20,30}
# print(a)
# for x in a:
#     print(x)