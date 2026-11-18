def reverse_n(n):
    neg=False
    if n<0:
        n*=-1
        neg=True
    result=0
    while n>0:
        result=result*10+n%10
        n//=10
    if neg:
        return result*-1
    else:
        return result
n=int(input('enter '))
print(reverse_n(n))