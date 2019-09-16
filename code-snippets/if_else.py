""" Sample program for using if-else statements"""

a="[ABC[23]][][89]"
ele=10
count=0
for x in range(ele,len(a)):
    if(a[x]=="["):
        count+=1
    elif(a[x]=="]"):
        count-=1
    else:
        pass
    if(count==0):
        print(x)
        break
