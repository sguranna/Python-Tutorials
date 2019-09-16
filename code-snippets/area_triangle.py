""" Program to find the area of a triangle given the three sides."""

import math

a = int(input("Enter the first side of a triangle"))
b = int(input("Enter the second side of a triangle"))
c = int(input("Enter the third side of a triangle"))

s=(a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The area of the triangle is :", area)