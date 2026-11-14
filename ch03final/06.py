n=(input("enter "))
n=n.split(",")
ans=""
for i in n :
    if int(i,2)%5==0:
        ans+=i+","
print(ans[:-1])

