num = int(input("enter number "))
if num <=0:
    print("invalid")
else:
    count=2
    while count<=num:
        divisor=1
        total=0
        while divisor<count:
            if count%divisor==0:
                total+=divisor            
            divisor+=1
        if total==count:
            print(count)
            
        count+=1
