for i in range(1,11):
    for k in range(i-1):
        print(" ",end="")
    for j in range(11-i):
        print("*",end="")
    print()

for i in range(1,11):
    for j in range(10-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()