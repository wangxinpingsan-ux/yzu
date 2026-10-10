topnum=int(input('enter number range '))
if topnum<=0:
    print("invalid")
else:
    num=2
    while num<=topnum:
        divisor=1
        total=0
        while divisor<num:
            if num%divisor==0:
                total+=divisor
            divisor+=1
        if total==num:
            print(f"{num} is perfect number")    
        num+=1
