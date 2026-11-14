s = input("enter sentence ")
c = -1
while True:
    i = s.find("t", c + 1)
    if i==-1:
        break
    print(i)
    c = i
