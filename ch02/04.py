num_range = int(input("enter number range "))
num=2
while True:
    divisor = 1
    sum_num = 0
    
    while num > divisor:
        if num % divisor == 0:
            sum_num += divisor
        divisor += 1
    if sum_num == num:
        print(f"{num} is perfect number")
    if sum_num < num:
        print(f"{num} is Deficient numbers")
    if sum_num > num:
        print(f"{num} is Abundant numbers")
    num+= 1
    
    if num>num_range:
        break
