# class Mobile:  # class definition
#     brand = "apple"
#     processor = "snapdragon"   # class variables
#     battery = 4000
#     camera=20

# # class variables by default applies to all objects.

# m1 = Mobile()   # create an object
# # print(type(m1))   # duck typing - creating user defined datatypes
# print(Mobile.camera)
# print(m1.battery)
# m1.brand = "mi"   # object variable
# print(id(m1.brand))
# print(id(Mobile.brand))
# print(m1.brand, Mobile.brand)
# m2 = Mobile()
# print(m2.brand)
# Mobile.brand = "samsung"
# m3 = Mobile()
# print(m3.brand)
# Mobile.screen = 5.6
# m4 = Mobile()
# print(m4.screen)
# mobiles = []
# for x in range(100):
#     a=Mobile()
#     mobiles.append(a)
# mobiles[4].camera=40
# print(mobiles[4].camera)


# class Mobile:
#     brand = "apple"
#     # constructor - special function, gets called 
#     # when creating an object. __init__().
#     def __init__(self, proc="snap", ram=4, battery=4000, cam=8):
#         self.processor = proc
#         self.camera = cam
#         self.Battery = battery
#         self.Ram = ram

#     def change_battery(self,batt):
#         self.Battery = batt

# Mobile.brand = "mi"
# m1 = Mobile("snap", 6, 2750, 20) # creating object
# # m1.create("snap", 6, 2750, 20)
# print(m1.processor)
# m1.screen = 5.6
# m2 = Mobile("mtk",4, 4000, 13)
# print(m2.processor)
# m3 = Mobile()
# print(m3.camera)
# # m3.change_battery(2350)
# Mobile.change_battery(m3,2350)  # alternate way of calling function
# print(m3.Battery)


# class Employee:
#     company="myntra"
#     hike = 1.1

#     def __init__(self, name, age, qual, salary):
#         self.name = name
#         self.age=age
#         self.qual=qual
#         self.salary = salary

#     def increase_pay(self):
#         self.salary = self.salary*self.hike

#     @classmethod
#     def change_details(cls):
#         cls.company = "flipkart"
#         cls.hike=1.7

#     @staticmethod
#     def fact(n):
#         f=1
#         for x in range(1,n+1):
#             f=f*x
#         return f

# e1=Employee("kumar", 25, "BTech", 30000)
# e2=Employee("raj", 34, "MTech", 90000)
# print(e1.salary)
# # e1.increase_pay()
# # print(e1.salary)

# Employee.change_details()
# print(e1.hike)
# e1.increase_pay()
# print(e1.salary)
# print(Employee.fact(6))
# print(e1.fact(6))
# print(e2.fact(100))


"""Inheritence - creating multiple classes from existing classes.
 1. All attributes(object/class variables) of base class will automatically
 apply for all sub classes.
 2. All functions available in base class can be used in sub class."""
# base class/ super class/ parent class - Employee
# child class/ sub class - Developer

# Method overloading - same function name, but different logic.
# class Developer(Employee):
#     def __init__(self, name, age, qual, salary, skill):
#         Employee.__init__(self,name, age, qual, salary)
#         self.skill = skill

#     def increase_pay(self):
#         print("developer method")
#         print(Employee.fact(20))
#         self.salary = self.salary*2

# class Manager(Employee):
#     def __init__(self, name, age, qual, salary, num_emps):
#         Employee.__init__(self,name, age, qual, salary)
#         self.num_emps = num_emps


# class Intern(Developer, Manager):
#     def __init__(self, name, age, qual, salary, skills, num_emps):
#         Developer.__init__(self,name, age, qual, salary, skills)
#         Manager.__init__(self, name, age, qual, salary, num_emps)



# i1 =Intern("shiva",25,"BTech",50000, "Python",15)
# # d1.skill = "Python"
# print(i1.salary)
# print(i1.salary, i1.num_emps)
# # d2 = Developer("raj",30, "MTEch", 30000, "C++")
# # d2.skill = "C++"


# class Distance:
#     def __init__(self, feet, inch):
#         self.feet = feet
#         self.inch=inch


    # def __add__(self, dist2):
    #     # print(self.feet, dist2.feet)
    #     # print(self.inch, dist2.inch)
    #     res_feet = self.feet+dist2.feet
    #     res_inch = self.inch + dist2.inch
    #     if(res_inch>12):
    #         res_inch=res_inch-12
    #         res_feet+=1
    #     d3 = Distance(res_feet, res_inch)
    #     return d3

        
# d1 = Distance(5, 7)
# d2 = Distance(3,6)
# # print(d1.feet
# # print(d2.inch)
# result=d1+d2

# # result=d1.add_dist(d2)  # alternative
# print(result.feet, result.inch)
# # d2.add_dist(d1)

class Sample:
    def __call__(self, a,b,c):
        self.name = a
        self.age=b
        self.qual=c
        print(a,b,c)
    
s = Sample()
s("name", 25, "BTech")  # calling function __call__() automatically
print(s.name, s.qual)
