s = input("enter ")
s = s.split(",")
a = ""
for i in range(len(s)):
    if int(str(s[i]), 2) % 5 == 0:
        a+=str(s[i])+","
print(a[0:-1])
