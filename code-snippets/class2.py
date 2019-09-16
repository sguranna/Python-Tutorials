# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def print_attr(self, list_stu):
#         for x in list_stu:
#             print(x.name, x.marks)

#     @classmethod
#     def compare_marks(self,list_stu):
#         marks = []
#         for x in list_stu:
#             marks.append(x.marks)
#         max_marks = max(marks)
#         ind = marks.index(max_marks)
#         print(list_stu[ind].name)
    
#     @staticmethod
#     def add(a,b):
#         return a+b
# s=[]
# for i in range(5):
#     name = eval(input("Enter the name"))
#     marks = eval(input("Enter the marks"))
#     if(marks>600):
#         print("marks should be below 600\n")
#         continue
#     s.append(Student(name, marks))
# s[0].print_attr(s)
# Student.compare_marks(s)
# #print(Student.add(3,5))

"""Inheritance: Inherit the attributes and methods from base class to derived class"""

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.email = name+'@gmail.com'

# class Developer(Employee):
#     def __init__(self,name, age, lang):
#         super().__init__(name, age)
#         self.lang = lang

# class Manager(Employee):
#     def __init__(self, name, age, num_emps):
#         super().__init__(name, age)
#         self.num_emps = num_emps

# class Intern(Developer, Manager):
#     def __init__(self, name, age, lang, num_emps,duration):
#         Developer.__init__(name, age, lang)
#         Manager.__init__(name, age, num_emps)
#         self.duration = duration
    
# # e1 = Developer("Ram", 25, "c++")
# # print(e1.email, e1.lang, e1.age)
# # m1 = Manager("Kumar", 32,10)
# # print(m1.email, m1.num_emps)
# i1 = Intern("shiva", 27, "c++",10, 6)
# print(i1.email)


# class Person:
#     def __init__(self, name, age):
#         self.name =name
#         self.age = age

# class Student:
#     def __init__(self, marks):
#         self.marks = marks

# class dummy(Person, Student):
#     def __init__(self, name, age, marks):
#         Person.__init__(self,name, age)
#         Student.__init__(self,marks)

# a=10
# print(type(a))
# d1 = dummy("Ram", 32, 568)
# print(type(d1))
# print(d1.name, d1.marks)

# Method overloading
# class sample:
#     def __init__(self, feet, inches):
#         self.feet  =feet
#         self.inches = inches
    
#     def __add__(self, s2):
#         f = self.feet + s2.feet
#         i = self.inches+s2.inches
#         if(i>12):
#             f+=1
#             i=i-12
#         s3 = sample(f,i)
#         return s3
# d1 = sample(4, 7)
# d2 = sample(3, 8)

# print((d1+d2).feet, (d1+d2).inches)
# Operator overloading - same operator, multiple functionalitis
# > - __gt__

class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def __gt__(self, s):
        return self.marks>s.marks
    
s1 = Student(578)
s2=Student(586)
s3=Student(548)

if(s1>s2 and s1>s3):
    print("s1 is topper")
if(s2>s1 and s2>s3):
    print("s2 is topper")
if(s3>s1 and s3>s2):
    print("s3 is topper")