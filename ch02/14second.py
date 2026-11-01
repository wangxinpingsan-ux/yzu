while True:
    n=int(input("enter "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    elif n==1:
        print("is not prime")
    else:
        prime=True
        d=2
        while d<n:
            if n%d==0:
                prime=False
                break
            d+=1
        if prime:
            print(f"{n} is prime")
        else:
            print(f"{n} is not prime")
            


