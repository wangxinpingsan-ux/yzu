x=int(input('enter range '))
if x<=0:
    print("invalid")
else:   
    y=2
    while y<=x:
        total=0
        i=1
        while i <y:   
            if y%i==0:
                total+=i
            i+=1
        if total==y:
            print(f"{y} is perfect number")
        elif total<y:
            print(f"{y} is Deficient number")
        else:
            print(f"{y} is Abundant numbers")
        y+=1