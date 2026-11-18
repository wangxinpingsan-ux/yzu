def factors(n):
    d = 1
    a = []
    while d < n:
        if n % d == 0:
            a.append(d)
        d += 1
    return a


def is_perfect(n):
    total = sum(factors(n))
    if total == n:
        return True
    else:
        return False


n = int(input("enter range "))
for i in range(2, n + 1):
    if is_perfect(i):
        print(i, end=" ")
        print("=","+".join(map(str,factors(i))))
        
