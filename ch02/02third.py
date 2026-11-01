while True:
    x=int(input("enter "))
    if x<=0:
        print("invalid")
    else:
        break



i=1
while i<=x:
    if x%i==0:
        print(i,end=" ")
    i+=1