import math
a=int(input("enter a "))
b=int(input("enter b "))
c=int(input("enter c "))
s=(a+b+c)/2
area=math.sqrt((s-a)*(s-b)*(s-c)*s)
print(f"{area:.2f}")
