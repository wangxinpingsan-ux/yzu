num=int(input("enter year "))
if num%4==0 and num%100!=0:
    print("leap year")
elif num%400==0:
    print("leap year")
else:
    print("is not leap year")