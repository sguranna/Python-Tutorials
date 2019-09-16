a=int(input("enter the number"))
b=int(input("enter the number"))

try:
    print(a/b)
    print("dbkadk")

except:
    b=1.0
    print(a/b)
    print("Enter denominator greater than 0")
finally:
    print("vnalnla")
    print("sjnall")

# # print(a+b)
# # print(a-b)


# a=[]
# # print(a[10])
# try:
#     print(a[10])
# except:
#     print("list should not be empty")


try:
    f=open("samplskahgukhe.txt","r")
except:
    f=open("samplekjkhfks.txt", "w")

