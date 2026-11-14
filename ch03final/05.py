n=input("enter ip ")
n=n.split(".")
if len(n)!=4:
    print("four decimal numbers")
else:
    if int(n[0])!=140 or int(n[1])!=138:
        print("invalid")
    elif int(n[2])<0 or int(n[2])>255:
        print("invalid")
    elif int(n[3])<0 or int(n[3])>255:
        print("invalid")
    else:
        print("valid")