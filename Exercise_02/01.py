w=int(input("enter w"))
x=int(input("enter x"))
y=int(input("enter y"))
z=int(input("enter z"))

avg=(w+x+y+z)/4

max_n=w
min_n=w

if x>max_n:
    max_n=x
if y>max_n:
    max_n=y
if z>max_n:
    max_n=z

if x<min_n:
    min_n=x
if y<min_n:
    min_n=y
if z<min_n:
    min_n=z

print(f"avg is {avg}\nmax is {max_n}\nmin is {min_n}")