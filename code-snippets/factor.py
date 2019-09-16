
"""Finding all the factors of a given number"""

n=int(input("enter a number"))
a=[]
for i in range(1, n+1):
    if(n%i==0):
        a.append(i)

for r in a:
    print(r)