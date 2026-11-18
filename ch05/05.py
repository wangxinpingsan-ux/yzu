def pi(n):
    n=2*n-1
    total=0
    i=1
    s=1
    while i<=n:
        total+=(4/i)*s
        i+=2
        s*=-1
    return total
while True:
    n=int(input("enter "))
    if n==0:
        break
    elif n<0:
        print("invalid")
    else:
        print(pi(n))