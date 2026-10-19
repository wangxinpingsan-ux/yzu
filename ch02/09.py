while True:
    n = int(input("enter number "))
    if n < 0:
        print("must>0")
    elif n == 0:
        break
    else:

        e = 2
        k = 1
        level = 1
        while k < n:
            level *= k + 1
            k += 1
            e += 1 / level
        print(e)
