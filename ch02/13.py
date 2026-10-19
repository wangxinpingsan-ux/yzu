while True:
    n=int(input("input n "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        i=1
        total=0
        while i<=n:
            total+=i*i
            i+=1
        print(total)
