while True:
    n=int(input('enter n '))
    if n==0:
        break
    elif n<0:
        print("invalid")
        continue
    else:
        e=1
        fi=1
        i=1
        while i <= n:
            e+=1/fi

            i+=1
            fi*=i
    print(e)
            