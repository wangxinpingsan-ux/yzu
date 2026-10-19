import math
a=1
count=0
while a <= 100000:
    i=math.sqrt(a+100)
    k=math.sqrt(a+268)
    if i==int(i) and k==int(k):
        print(a)
        count+=1

    a+=1
print(f"total is {count}")