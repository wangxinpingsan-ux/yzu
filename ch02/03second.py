num = int(input("enter number "))
if num==0:
    print(num)
if num < 0:
    print("-", end="")  
    num = -num
n = 1
while n <= num:
    n *= 10

n //= 10
while n >= 1 :
    print(int(num // n), end="    ")
    num -= (num // n) * n
    n //= 10
