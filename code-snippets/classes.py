# class Employee:
#     raise_amount = 1.1
#     def __init__(self,name, age, pay):
#         self.name = name
#         self.age = age
#         self.pay = pay
    
#     @classmethod
#     def change_raise(cls):
#         cls.raise_amount  =1.2
    
#     def change_pay(self):
#         self.pay = self.pay * self.raise_amount

# class Manager(Employee):
#     def __init__(self, name, age, pay, employees=None):
#         Employee.__init__(self, name, age, pay)
#         if employees == None:
#             self.employees=[]
#         else:
#             self.employees = employees
    
# class Developer(Employee):
#     def __init__(self, name, age, pay, lang):
#         Employee.__init__(self, name, age, pay)
#         self.lang = lang

# d1 = Developer("ram",25, 20000, "python")
# d2 = Developer("shiva", 35, 50000, "c++" )
# print(d1.lang)

#Add two distance in feet and inches.

# class Distance:
#     def __init__(self,feet, inches):
#         self.feet = feet
#         self.inches = inches
#     @staticmethod
#     def add_dist(dist1, dist2):
#         dist3 = (dist1.feet + dist2.feet)
#         dist4 = dist1.inches + dist2.inches
#         return dist3, dist4
# d1 = Distance(3, 5)
# d2 = Distance(10, 3)
# print(d1.feet)
# res1, res2 = Distance.add_dist(d1, d2)
# print(res1, res2)


# class Explore1:
#     def explore(self):
#         print("Explore method of Explore1 class")
    
# class Explore2(Explore1):
#     def explore(self):
#         print("Explore method of Explore2 class")

# class Explore3:
#     def explore(self):
#         print("Explore method of Explore3 class")

# e = Explore2()
# e.explore()

# class Student:
#     def __init__(self, rollno, name):
#         self.rollno = rollno
#         self.name = name
    
#     def show(self):
#         print(self.rollno, self.name, self.age)
    
#     def set_age(self, age):
#         self.age = age

# s1 = Student(1234, "ram")
# s1.age = None
# s1.set_age(25)
# s1.show()

# class Student:
#     pass

# a=10
# print(type(a))
# s1 = Student()
# print(type(s1))

"""Duck typing -  Creating user defined datatypes.
Existing datatypes: int, float, string, complex, bool, list, dict, tuple
"""
# class Pycharm:
#     def ide(self):
#         print("Executing")
    
# class Laptop:
#     def code(self, ide1):
#         print("done")
    
# ide1 = Pycharm()
# l1 = Laptop()

# l1.code(ide1)
# print(type(ide1), type(l1))

"""
Method overloading - Same function name, but different arguments, diffrent definition.
Operator overloading - Same operator, but different funcionality.
+ - __add__(), * - __mul__(), /- __div__()
"""

# class Student:
#     def __init__(self, marks1, marks2):
#         self.m1 = marks1
#         self.m2 = marks2
#     def __add__(self, other):
#         mark1 = self.m1 + other.m1
#         mark2 = self.m2 + other.m2
#         s3 = Student(mark1, mark2)
#         return s3
#     def __gt__(self, other):
#         total1 = self.m1 + self.m2
#         total2 = other.m1 + other.m2
#         if(total1>total2):
#             return True
#         else:
#             return False
    
    
# s1 = Student(78, 65)
# s2 = Student(98, 54)
# #s3 = s1+s2

# if(s1>s2):
#     print("s1 wins")
# else:
#     print("s2 wins")
# #print(s3.m1, s3.m2)

