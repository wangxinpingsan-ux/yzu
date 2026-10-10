grade = int(input("enter grade "))
count = 0
total = 0
while True:
    if grade == -1:
        break
    elif grade > 100 or grade < 0:
        print("invalid")
    else:
        total += grade
        count += 1
    grade = int(input("enter grade "))
if count == 0:
    print("no grade")
else:
    print(total / count)
