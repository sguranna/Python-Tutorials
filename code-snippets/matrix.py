#2x3 matrix using list. Take inptus from the user.
a=[]
for x in range(2):
    b = [] 
    for y in range(3):
        temp = int(input("Enter the matrix elements row-wise"))
        b.append(temp)
    a.append(b)
    print(a)
print(a)

d=[]
for x in range(2):
    b = [] 
    for y in range(3):
        temp = int(input("Enter the matrix elements row-wise"))
        b.append(temp)
    d.append(b)
    print(d)
print(d)
res = []
for x in range(len(a)):
    b = []
    for y in range(len(a[0])):
        b.append(a[x][y]+d[x][y])
    res.append(b)
