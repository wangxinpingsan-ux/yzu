while True:
    n=int(input("enter range "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        total=0
        i=1
        x=1
        fi=1
        while x<=n:
            while i<=x:
                fi*=i
                total+=fi
                i+=1
            x+=1
        print(total)