def pi (n):
    n=2*n-1
    i=1
    total=0
    s=1
    while i<=n:
        total+=(4/i)*s
        i+=2
        s*=-1
    return total
n=int(input("enter "))
print(pi(n))