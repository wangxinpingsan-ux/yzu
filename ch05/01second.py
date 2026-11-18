def is_prime(i):
    prime=True
    d=2
    if i==1:
        prime=False
    while d<i:
        if i%d==0:
            prime=False
            break
        d+=1
    return prime
n=int(input("enter range "))
count=0
a=[]
for i in range(1,n+1):
    if is_prime(i):
        a.append(str(i))
        count+=1
print(",".join(a))
print(count)