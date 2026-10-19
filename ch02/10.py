while True:
    num=int(input("prime range "))
    if num==0:
        break
    elif num<0:
        print("invalid")
        continue
    elif num==1:
        continue
    else:
        i=2     
        while i<=num:
            n=2
            prime=True
            while n<i:
                if i%n==0:
                    prime=False
                    break
                n+=1
            if prime:
                print(i,end=" ")
            i+=1
        print()
 