first = 0
second = 1
num = int(input("enter number "))


if num < 0:
    print("invalid")
elif num == 0:
    print(first)
elif num == 1:
    print(second)
else:
    total = 0
    count = 1
    while count < num:
        total = first + second
        count += 1
        first = second
        second = total
    print(total)
