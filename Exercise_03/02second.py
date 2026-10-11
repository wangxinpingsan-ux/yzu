num=int(input("enter number "))
a=0
b=1
if num<0:
    print("invalid")
elif num==0:
    print(a)
elif num==1:
    print(b)
else:
    count=1
    total=1
    while count<num:
        total=a+b
        a,b=b,total
        count+=1
    print(total)