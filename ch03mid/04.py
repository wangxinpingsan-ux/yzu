s=input("input world ")
key=["a","e","i","o","u"]
count=0
for i in s.lower():
    if i in key:
        count+=1
print(count)