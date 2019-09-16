# class Mobile:   # creating class
#     brand = "Apple"

#     """Constructor"""
#     def __init__(self, camera=20, battery=4000, processor="snap", ram="8gb"):  
#         self.camera = camera
#         self.processor = processor
#         self.battery =  battery
#         self.ram = ram

#     """Instance method/ Object method"""
#     def pic(self, dummy):
#         print("taking picture", dummy)
    
#     """Class method"""
#     @classmethod
#     def change_brand(cls, brand):
#         cls.brand = brand

#     @staticmethod
#     def factorial(n):
#         fac=1
#         for x in range(1,n+1):
#             fac = fac*x
#         return fac

#     @staticmethod
#     def add(a,b):
#         return a+b

# m=Mobile("20mp", "4000mah", "snap", "8gb")
# n=10
# fact = m.factorial(n)
# print(fact)
# print(m.add(3,4))
# m2=Mobile()

"""Inheritence"""
# Creating sub classes from main class. All attributes and methods
# of main class will automatically come to subclass.
# Subclass can have extra attributes and methods.

# class Mobile:
#     def __init__(self, processor, battery, brand):
#         self.battery = battery
#         self.processor = processor
#         self.brand = brand
    

# class baiscmobile(Mobile):
#     pass
    # def add_camera(self, camera):
    #     self.camera = camera
    #     print("sub class method")

# class smartphone(Mobile):
#     def __init__(self, processor, battery, brand, camera):
#         super().__init__(processor, battery, brand)
#         self.camera = camera

# class sample(smartphone):
#     sample_var = "dummy"

# m = Mobile("mtk", "2300", "samsung")
# bm = baiscmobile("mtk", "3000", "samsung")
# print(bm.battery)
# sm = smartphone("mtk", "4000", "apple", "20mp")
# print(sm.processor, sm.camera)

# s1 = sample("i7", "3000", "mi", "12mp")
# print(s1.sample_var)

# class sample1(smartphone, baiscmobile):
#     def __init__():
#         baiscmobile.__init__()

# class Base1:
#     def __init__(self, name, age):
#         self.name = name
#         self.age=age

# class Base2:
#     def __init__(self, gender, sal):
#         self.gender = gender
#         self.sal = sal
# class Base3:
#     pass
# class emp(Base1, Base2, Base3):
#     def __init__(self, name, age, gender, sal, lang):
#         Base1.__init__(self, name, age)
#         Base2.__init__(self, gender, sal)
#         self.lang = lang

# e1 = emp("kumar",24, "Male", 20000, "python")
# print(e1.name, e1.age, e1.sal, e1.gender, e1.lang)

"""Ploymorphism"""
""" Single name- many forms """
"""Method Overloading"""


# class sample:
#     def add(self):
#         print("this is a method of sample class")
    
# class sample2:
#     def __init__(self, m1, m2, m3, m4):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#         self.m4=m4

#     def add(self):
#         print("this is methos of sample2 class")
#     def sum(self):
#         marks = self.m1+self.m2+self.m3+self.m4
#         print(marks)

# stu1 = sample2(97,87,76,98)
# stu1.sum()


# obj1 = sample()
# obj2 = sample2()

# obj1.add()
# obj2.add()
# a=[10,20,30]
# print(sum(a))

# class distance:
#     def __init__(self, feet, inch, cm):
#         self.feet = feet
#         self.inch = inch
#         self.cm = cm

#     def __add__(self,dist):
#         feet_res = self.feet + dist.feet
#         inch_res = self.inch + dist.inch
#         cm_res = self.cm + dist.cm
#         if inch_res>12:
#             feet_res+=1
#             inch_res = inch_res-12
#         d3 = distance(feet_res, inch_res, cm_res)
#         return d3

# d1 = distance(2,6, 30)
# d2 = distance(5,8, 40)
# print(d1.feet)
# print(d1.feet, d1.inch, d2.feet, d2.inch)
# d3 = d1.__add__(d2)
# # d3=d1+d2
# print(d3.feet, d3.inch)
# # d2.add(d1)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print("done")

s = Student("fhdh","llkwhru")
print(s.fname, s.lname)
