def reverse(n):
    result=0
    sign=True
    if n <0:
        n*=-1
        sign=False
    while n>=10:
        result+=n%10
        n//=10
        result*=10
    result+=n
    if sign:
        return result
    else:
        return result*-1
n=int(input("enter "))
print(reverse(n))

    