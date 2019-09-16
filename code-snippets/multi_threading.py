# import time
# # from threading import Thread

# # class Hello(Thread):
# #     def run(self):
# #         for i in range(5):
# #             time.sleep(1)
# #             print("Hello")

# # class Hi(Thread):
# #     def run(self):
# #         for i in range(5):
# #             time.sleep(1)
# #             print("Hi")

# # class sample(Thread):
# #     def run(self):
# #         for i in range(5):
# #             time.sleep(1)
# #             print("sample")

# # o1 = Hello()
# # o2 = Hi()
# # o3 = sample()
# # stime = time.time()
# # o1.start()
# # o2.start()
# # o3.start()
# # etime = time.time()
# # print(etime-stime)

# # def hello():
# #     for x in range(10):
# #         print("Hello")
    
# # def hi():
# #     for x in range(10):
# #         print("Hi")

# # t1 = Thread(target=hello, args=(name,))
# # t2 = Thread(target=hi)

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()

# # print("Done")

# # from multi_threading import Thread
# from multiprocessing import Process

# def hello(name, age):
#     for x in range(10):
#         time.sleep(1)
#         print("Hello, "+name)
    
# def hi(name, age):
#     for x in range(10):
#         time.sleep(1)
#         print("Hi, "+name)
# name="Kumar"
# age=20
# p1 = Process(target=hello, args=(name,age))
# p2 = Process(target=hi, args=(name,age))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print("done")

# import threading
# import time

# result = None
# def hello(name):
#     for i in range(10):
#         time.sleep(1)
#         print("hello, "+name)
#     global result
#     result=i
# def hi():
#     for i in range(10):
#         time.sleep(1)
#         print("hi")

# def sample():
#     for i in range(10):
#         time.sleep(1)
#         print("sample")
    
# # hello()
# # hi()
# name ="shiva"
# t1 = threading.Thread(target=hello, args=(name,))
# t2 = threading.Thread(target=hi)
# t3 = threading.Thread(target=sample)
# st =time.time()
# t1.start()
# t2.start()
# t3.start()
# print("done")
# t1.join()
# t2.join()
# t3.join()
# et=time.time()
# print(et-st)
        
# import multiprocessing
# import time

# class sample(multiprocessing.Process):
#     def run(self):
#         for i in range(10):
#             time.sleep(0.2)
#             print("sample")

# class sample2(multiprocessing.Process):
#     def run(self):
#         for i in range(10):
#             time.sleep(0.2)
#             print("hello")

# c1 = sample()
# c2= sample2()   
# # st=time.time()
# # c1.run()
# # c2.run()
# c1.start()  # starting a thread or process
# c2.start()
# c1.join()
# c2.join()
# et=time.time()
# print(et-st)

# from multiprocessing import Process
# import multiprocessing
# import time
# #Thread, Process

# balance = 1000
# def hello(val):
#     for x in range(5):
#         time.sleep(1)
#         print("hello")
#         val.put(100)

# def hi(val):
#     for x in range(5):
#         time.sleep(1)
#         print("hi")
#         val.put(200)
#         print(val.get())

# val = multiprocessing.Value("i")
# que = multiprocessing.Queue("i")
# val =1000
# p1 = Process(target=hello, args=(que,))
# p2 = Process(target=hi, args=(que,))
# st = time.time()
# p1.start()
# p2.start()
# print(val)
# p1.join()
# p2.join()
# et=time.time()
# print(et-st)


# from multiprocessing import Pool
# import time
# p = Pool(2)
# x=list(range(1000000))
# #print(x)

# def sample(inp):
#     for i in inp:
#         print(i*2)

# st = time.time()
# for t in x:
#     print(t*2)
# et = time.time()
# print(et-st)

# st = time.time()
# map(sample,x)
# et = time.time()
# print(et-st)

# import multiprocessing
# import time

# result = []

# def sample():
#     for x in range(10):
#         result.append(10)
#         time.sleep(0.2)
#         print("sample")
#     print(result)        

# def sample2():
#     for x in range(100000000):
#         result.append(100)
#         time.sleep(0.2)
#         print("hello")

# # sample()
# # sample2()

# p1 = multiprocessing.Process(target=sample, args=())
# p2 = multiprocessing.Process(target=sample2)

# p1.start()
# # t1.join()
# p2.start()
# p1.join()  # wait till this thread is completed
# print("fkgyjkf")
# p2.join()
# print(result)
# print("done")