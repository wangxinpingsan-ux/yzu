def is_prime (n):
    if n==1:
        return False
    d=2
    while d<n:
        if n%d==0:
            return False
        d+=1
    return True
        
    
n=int(input("enter range "))
count=0
a=[]
for i in range(2,n+1):
    if is_prime(i):
        count+=1
        a.append(str(i))
print(",".join(a))
print(count)
