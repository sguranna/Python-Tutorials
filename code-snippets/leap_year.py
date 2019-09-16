n = int(input("Enter any year to find out whether it is leap year or not:"))

if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print(f"{n} is a leap year")
        else:
            print(f"{n} is not a leap year")
    else:
        print(f"{n} is a leap year")
else:
    print(f"{n} is not a leap year")