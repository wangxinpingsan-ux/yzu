total=0
count=0
while True:
    grade=int(input("enter grade "))
    if grade ==-1:
        break
    elif grade<0 or grade>100:
        print("invalid") 
    else:
        total+=grade
        count+=1
if count==0:
    print("0")
else:
 print(total/count)