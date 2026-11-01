x=int(input("enter "))
if x==0:
    print(0)
elif x <0:
    print("-",end='')
    x=-x
i=1
while i<=x:
    i*=10
i//=10
while i >=1:
    print(x//i,end='    ')
    x-=i*(x//i)
    i//=10
    
