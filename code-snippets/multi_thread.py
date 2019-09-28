# multithreading
# parallelizing the functions.
# creating the thread for every function.
# Starting all the threads.
# Joining all the threads.
# By default, every program will have main thread.

# import threading
# import time
# import multiprocessing

# a=100
# b=200

# def add(x):   
#     global a
#     a=1000
#     for i in range(5):
#         time.sleep(0.3)
#         print("addition", a,b)

# def sub():
#     for i in range(15):
#         time.sleep(0.3)
#         print("subtraction",a,b)

# def mul():
#     for i in range(10):
#         time.sleep(0.3)
#         print("multiplication",a,b)

# t1 = threading.Thread(target=add, args=(10,), daemon=True)
# t2 = threading.Thread(target=sub)
# t3 = threading.Thread(target=mul)

# t1.start()   # starts the function execution and go to next line
# t2.start()   # start the second function execution
# t1.join()
# t2.join()
# t3.start()  # start the third function execution.

# # all 3 functions are running parallelly.
# # no need for closing the threads, threads will get closed
# # automatically once the function execution finishes.

# # join() - if you have any statements to be executed after
# # finishing of the threads, then you need to use join().

# #t1.join() # control will wait here till t1 gets finished
# #t2.join() # control will wait here till t2 gets finished
# t3.join() # program flow will wait here till t3 gets finished.

# print("done")


# class Hello(threading.Thread):
#     def run(self):
#         for i in range(5):
#             # time.sleep(1)
#             print("Hello")

# class Hi(threading.Thread):
#     def run(self):
#         for i in range(5):
#             # time.sleep(1)
#             print("Hi")

# class sample(threading.Thread):
#     def run(self):
#         for i in range(5):
#             # time.sleep(1)
#             print("sample")

# o1 = Hello()
# o2 = Hi()
# o3 = sample()
# stime = time.time()
# o1.run()
# o2.run()
# o3.run()
# # o1.join()
# # o2.join()
# # o3.join()
# etime = time.time()
# print(etime-stime)


# import threading 
  
# # global variable x 
# x = 0
  
# def increment(): 
#     """ 
#     function to increment global variable x 
#     """
#     global x 
#     x += 1
  
# def thread_task(lock): 
#     """ 
#     task for thread 
#     calls increment function 100000 times. 
#     """

#     for _ in range(100000):
#         lock.acquire() 
#         increment()
#         lock.release() 
  
# def main_task(): 
#     global x 
#     # setting global variable x as 0 
#     x = 0

#     lock = threading.Lock()
#     # creating threads 
#     t1 = threading.Thread(target=thread_task, args=(lock,)) 
#     t2 = threading.Thread(target=thread_task, args=(lock,)) 
  
#     # start threads 
#     t1.start() 
#     t2.start() 
  
#     # wait until threads finish their job 
#     t1.join() 
#     t2.join() 
  
# if __name__ == "__main__": 
#     for i in range(10): 
#         main_task() 
#         print("Iteration {0}: x = {1}".format(i,x))

# import multiprocessing
# import time

# a=100
# b=200
# # a = multiprocessing.Value("i", 100)
# q = multiprocessing.Queue()

# def add(x):  
#     while(1):
#         time.sleep(0.3)
#         x.put(100)
#         if():
#             break

# def sub():
#     for i in range(15):
#         time.sleep(0.3)
#         print("subtraction",a,b)

# def mul():
#     for i in range(10):
#         time.sleep(0.3)
#         print("multiplication",a,b)

# p1 = multiprocessing.Process(target=add, args=(q,))
# p2 = multiprocessing.Process(target=sub)
# p3 = multiprocessing.Process(target=mul)

# p1.start()
# p2.start()
# p3.start()
# p1.join()
# p2.join()
# p3.join()
# print(q)
# while(!q.empty):
#     print(q.get())


from multiprocessing import Pool
import time
def f(n):
    return n*n

if __name__ == "__main__":
    # p = Pool(processes=10)
    s = time.time()
    x = list(range(100000))
    result = map(f,x)
    # for i in x:
    #     res = f(i)
    #     print(res)
    e = time.time()
    print(e-s)
    # result = map(f,x)
    # for n in result:
    #     print(n)


# def foo(bar, baz):
#   print( 'hello {0}'.format(bar))
#   return 'foo' + baz

# from multiprocessing.pool import ThreadPool
# pool = ThreadPool(processes=4)

# async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo

# # # do some other stuff in the main process

# return_val = async_result.get()  # to get the return value from function.
# print(return_val)
