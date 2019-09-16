""" Function definition and usage"""
# def list_create(n):
#     a=[]
#     for x in range(n):
#         a.append(x*x)
#     print(a)

# print("fkfuhriul")
# n = eval(input("enter the number"))
# list_create(n)
# print("done")

""" Sample add function """
# def add():
#     """this is an addition function"""
#     a=10
#     b=20
#     c=a+b
#     print(c)
#     # return c

# result = add()
# print(result)

""" Builtin function sum()"""
# a=[10,20,30,40]
# print(sum(a))

""" Scope of a variable is not applicable for code blocks 
like if conditions and loops. Variables will always bind to 
the scope of the innermost function/class"""
# a=10
# if(a>5):
#     x=20
#     y=30
# print(x)

# a=2
# for x in range(a):
#     print(x)
# print(x)

""" Example depicting the use of global and nonlocal keywords"""
# a=10  # gloabl bariables
# b=20
# def add(a,b):
#     # print(res)
#     global res
#     res = 200
#     # print(res)
#     x=20
#     def sample():
#         nonlocal x
#         global res
#         x=200
#     sample()
#     print(x)
# add(a,b)
# print(a,b)
# print(res)
# print(x)

""" Function overloading is not supported in python"""
# def sample(x):
#     print(x)

# def sample(x,y):
#     print(x+y)

# x=10
# y=20
# # sample(x)
# sample(x,y)