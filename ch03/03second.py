s=input("input ")
count=0
s_len=len(s)
for i in range(s_len):
    for j in range(s_len):
        for k in range(s_len):
            if i==j or i==k or j==k:
                continue
            print(s[i],s[j],s[k],sep='',end=" ")
            count+=1
print(count)
