def add(n):
    total=0
    while n>=10:
        total+=n%10
        n//=10
    return total+n
n=int(input("enter "))
print(add(n))