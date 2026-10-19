theyear=int(input("enter year "))
if theyear%4==0 and theyear%100!=0:
    print("leap year")
elif theyear%400==0:
    print("leap year")
else:
    print("no leap year")