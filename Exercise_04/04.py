while True:
    num=int(input("enter range "))
    if num==0:
        break
    elif num<0:
        print("invalid")
        continue
    else:
        i=2
        while i<=num:
            d=2
            prime=True
            while d<i:
                if i%d==0:
                    prime=False
                    break
                d+=1
            if prime:
                print(i,end=" ")
            i+=1
        print()
