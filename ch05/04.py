def is_perfect(i):
    d=1
    total=0
    while d<i:
        if i%d==0:
            total+=d
        d+=1
    if total==i:
        return True
    else:
        return False
def factors(i):
    a=[]
    d = 1
    while d < i:
        if i % d == 0:
            a.append(str(d))
        d += 1
    return a
n=int(input("enter "))
for i in range(2,n+1):
    if is_perfect(i):
        print(i,end=" ")
        print("+".join(factors(i)))