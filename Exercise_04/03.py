while True:
    num=int(input("enter number "))
    if num==0:
        break
    elif num<0:
        print("invalid")
        continue
    else:
        i=1
        fi=1
        total=0
        while i<=num:
            fi*=i
            i+=1
            total+=fi

        print(total)

