while True:
    n=int(input("enter range "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    elif n==1:
        continue
    else:
        count=0
        topnumber=2
        while topnumber<=n:
            i=2
            prime=True
            while i<topnumber:
                if topnumber%i==0:
                    prime=False
                    break          
                i+=1
            if prime:
                print(topnumber,end=",")
                count+=1
            topnumber+=1
        print()
        print(count)
    

        
        