while True:
    x=int(input("enter number "))
    if x==0:
        break
    elif x<0:
        print("invalid")
    else:
        i=1
        total=1
        while i<=x:
            total*=i
            i+=1
        print(total)