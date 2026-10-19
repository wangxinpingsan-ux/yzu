total=0
count=0
while True:
    
    grade=int(input("enter grade "))
    if grade==-1:
        print(total//count)
        break
    if grade<0 or grade>100:
        print("invalid")
    else:
        total+=grade
        count+=1