import sys
# a=eval(input("Enter the number"))
# print(a, type(a))


# int(), str(), list()

# a,b,c=list((map(eval, input("enter the numbers").split(","))))
# print(a,b,c)

# a=(12,"fgufh", 34)
# x,y,z=a
# print(x,y,z)
def sample(x,y):
    print(x,y)

# import argparse

# parser = argparse.ArgumentParser(description="helop section")
# parser.add_argument("--num1","-a", help="some number", type=int)
# parser.add_argument("-b",default=20, help="some number", type=int)
# args = parser.parse_args()
# # sample(args.num1,args.num2)

# print(args)

x=eval(sys.argv[1])
y=eval(sys.argv[2])
print(sys.argv)
print(type(x))
