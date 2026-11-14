s=input("input ")
s=s.lower()
count=0
key=["a","e","i","o","u"]
for i in s:
    if i in key:
        count+=1
print(count)