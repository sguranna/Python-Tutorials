print("Enter the three numbers for finding the largest among them")
a=int(input())
b=int(input())
c=int(input())
print(a,b,c)
if((a>b) and (a>c)):
    print(f"{a} is the largest")
elif((b>a) and (b>c)):
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")