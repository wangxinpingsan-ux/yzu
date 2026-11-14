s=input("enter ")
s=s.split()
a=[]
for i in range(len(s)):
    s[i]=s[i][::-1]
    a.append(s[i])
print(" ".join(a))