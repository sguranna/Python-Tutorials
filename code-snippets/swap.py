a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

print(f"The numbers you have entered are a:{a}, b:{b}")

# ### using 3rd variable ####
# temp = a
# a=b
# b=temp
# print(f"The numbers after swap are a:{a}, b:{b}")


# ###  Using +,- combination ####
# a=a+b
# b=a-b
# a=a-b
# print(f"The numbers after swap are a:{a}, b:{b}")

# ###  Using *,/ combination. This works only for numbers greater than 0 ####
# a=a*b
# b=a/b
# a=a/b
# print(f"The numbers after swap are a:{a}, b:{b}")


### the python way ####
a,b = b,a
print(f"The numbers after swap are a:{a}, b:{b}")