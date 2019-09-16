# import json

# def read_file():
#     f = open("string_output.txt",'r')
#     #a={"name":"besant","age":20}
#     a = json.load(f)
#     print(a)
#     f.close()

# read_file()

# first method of opening a file
# a=["12\n","34\n","56\n","hello\n"]
# f=open("/home/shiva/Pictures/1.txt","r")
# #f.writelines(a)
# d=f.read(5)
# print(d)
# print(f.tell())
# f.seek(10)
# print(f.read())
# f.close()
# d=f.read(100)
# print(d)
# for x in f:
#     print(x)
# d =f.readlines()
# print(d[3])
# f.close()

# # Second method of opening a file
# with open("/home/shiva/shiva/python/string_output.txt", "r") as f:
#     d=f.readline()
#     print(d)


# a=[]
# for x in range(100):
#     a.append(input("Enter the number"))

# print(a)

# f=open("/home/shiva/Pictures/button.jpeg", "rb")
# a=f.read()
# f2 = open("sample.jpeg","wb")
# f2.write(a)
# f.close()
# f2.close()

# f = open("writejdghkih.txt", "w+")
# print(f.read())
# f.write("vkffhff\n")
# f.close()

# import json
# f = open("sample.json", "w")
# # Total file content should be a single variable
# a=[{"skhf":"kbafjkn", "jskjfh":[12,43,5,46,757]}]
# print(a)
# json.dump(a,f)
# f.close()

# f = open("sample.json", "r")
# a=json.load(f)
# print(type(a))


"""Opening anf closing"""

# f = open("dummy.txt","a+")
# a=f.readlines()
# print(a)
# f.write("kdlldjhgelahgeahn\n")
# f.close()

# f = open("/home/shiva/Pictures/button.jpeg","rb")
# a = f.read()
# f2 = open("button2.jpeg","wb")
# f2.write(a)
# f2.close()
# f.close()

"""seek and tell"""
f=open("dummy.txt","r")
print(f.read(4))
print(f.tell())
f.seek(0,1)      #Use case?  
print(f.tell())
# print(f.read(10))
# print(f.tell())
# f.read(5)
# print(f.tell())
f.close()

"""Json files"""
# import json

# f=open("dummy.json", "w")
# a={"name":"shiva", "age":25, "sal":20000, "dummy":[2,"glfdj",3545]}
# b=[2,"glfdj",3545]
# json.dump(a,f)
# json.dump(b,f)
# f.close()

# f = open("dummy.json", "r")
# a=json.load(f)
# print(a)