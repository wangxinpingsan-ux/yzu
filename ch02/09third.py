while True:
    n=int(input("input n "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        e=1
        i=1
        fi=1
        while i<=n:
            fi*=i
            e+=(1/fi)
            i+=1
        print(e)
