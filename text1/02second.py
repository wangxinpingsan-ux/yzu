num = int(input("enter number "))
if num <= 0:
    print("invalid")
else:
    n = 1
    while n <= num:
        if num % n == 0:
            print(n, end=" ")
        n += 1
