while True:
    n=int(input("enter range "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        end=1
        total=0
        while end<=n:
            d=0
            x=end
            while x >=10:
                i=x%10
                d+=i
                x//=10
            d+=x
            if end%d==0:
                print(end,end=" ")
                total+=1
            end+=1
        print()
        print(f"total = {total}")