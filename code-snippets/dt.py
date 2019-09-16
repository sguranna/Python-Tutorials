# import datetime
# import time
# for x in range(100):
#     dt = datetime.datetime.now()
#     print(str(dt))
#     time.sleep(1)
#     f = open(str(dt)+'.txt', 'w')
#     f.write(str(dt))
#     f.close()


# import time


# stime = time.time()
# for x in range(10):
#     time.sleep(1)
# etime = time.time()
# print(etime-stime)




import datetime
import time
f =open("samplefile.txt", "w")
# dt = datetime.datetime.now()
# f.write(str(dt))
# f.close()
start_time = time.time()
sum=0
for x in range(50036593813):
    # time.sleep(1)
    sum=sum+1
    print("done")
    f.write(str(datetime.datetime.now()))
    f.write(" :"+str(sum)+"\n")
f.close()
end_time = time.time()
print("time taken for loop:", end_time-start_time)