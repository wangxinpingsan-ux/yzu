num = int(input("enter number "))
if num < 0:
    print("invalid")
else:
    c = 1
    while c <= num:

        n = 1
        total = 0
        while n < c:
            if c % n == 0:
                total += n
            n += 1
        if total == c:
            print(c, end=" ")
        c += 1
