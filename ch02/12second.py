import math
a=1
while a<=100000:
    x=int(math.sqrt(a+100))
    y=int(math.sqrt(a+268)) 
    if x*x== a+100 and y*y==a+268:
        print(a)
    a+=1