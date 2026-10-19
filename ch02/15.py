while True:
    n=int(input("input n "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        k=1
        total=0
        fi=1
        while k<=n:
            fi*=k
            k+=1
            total+=fi
        print(total)
