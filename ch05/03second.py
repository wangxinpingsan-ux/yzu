def sumdight(n):
    total=0
    while n>=10:
        total+=n%10
        n//=10
    total+=n
    return total
n=int(input("enter "))
print(sumdight(n))