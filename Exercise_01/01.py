number=int(input("enter five-digit number:"))
c1=number%10
number//=10
c2=number%10
number//=10
c3=number%10
number//=10
c4=number%10
c5=number//10
print(f"{c5}   {c4}   {c3}   {c2}   {c1}")
