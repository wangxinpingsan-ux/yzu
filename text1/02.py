while True:
    num = int(input("enter number "))
    if num <= 0:
        print("num must >0 ")
    else:
        break

n = 1
while n <= num:
    if num % n == 0:
        print(n)
    n += 1
