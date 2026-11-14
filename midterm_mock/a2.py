s=input("input s ")
c=input("input c ")
index=""
count=0
removed=""
for i,k in enumerate(s):
    if k==c:
        index+=str(i)+" "
        count+=1
    else:
        removed+=k
print(f"index: {index}")
print(f"count: {count}")
print(f"removed: {removed}")