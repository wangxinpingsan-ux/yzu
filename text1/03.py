num = int(input("enter number"))
n = 1
if num < 0:
    num = -num
    print("-", end="")
while True:
    if num >= n * 10:
        n = n * 10
    else:
        break
while True:
    if n>=1:
        x = num // n
        print(x, end="    ")
        num = num - x * n
        n = n // 10
    else:
        break
