while True:
    num = int(input("input num "))
    if num == 0:
        break
    elif num < 0:
        print("invalid")
    elif num == 1:
        print(f"{num} is not a prime number")
    else:
        i = 2
        prime = True
        while i < num:
            if num % i == 0:
                prime = False
                print(f"{num} is not a prime number")
                break

            i += 1
        if prime:
            print(f"{num} is a prime number")
