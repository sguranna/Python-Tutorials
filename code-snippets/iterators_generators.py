# # a=(10,20,30)

# # it = iter(a)

# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())

# def ranges():
#     x=0
#     print("first call")
#     yield x
#     x=x+2
#     print("second call")
#     yield x
#     x=x+2
#     print("third call")
#     yield x

# # for x in ranges():
# #     print("call")
# #     print(x)
# # x=ranges()
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # print(next(x))
# # for x in ranges():
# #     print(x)
# # x =ranges()
# # print(x)
# # print(list(x))
# #print(ranges())

# # class Range:
# #     def __iter__(self, initial,  limit):
# #         self.initial = initial
# #         self.limit=limit

# #     def __next__(self):
# #         prev = self.initial
# #         if(self.initial==self.limit):
# #             return "Stopped"
# #         else:
# #             print("reached here")
# #             self.initial +=1
# #             return (prev**2)

    
# # a=Range()
# # a.__iter__(1,5)
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())
# # print(a.__next__())


# a=(10,20,304,3,5,506,0,76)
# # b = iter(a)
# b=a.__iter__()
# print(type(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(b.__next__())



fun = (x*2 for x in range(10) if x%2==0)
b=fun
# print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
