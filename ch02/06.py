num=int(input("enter number "))

while num!=0:
    
    if num<0:
        print("invalid") 
    else:
        total=num
        while True:
            if num==1:
                break
            total=total*(num-1)    
            num-=1
        print(total)
    num=int(input("enter number "))
    
