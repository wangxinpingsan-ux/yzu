num=int(input('enter number '))
while num!=0:
    if num <0:
        print("invalid")
    else:
        total=num
        num=num-1
        while num>0:
            total*=num
            num-=1
        print(total)
    num=int(input('enter number '))