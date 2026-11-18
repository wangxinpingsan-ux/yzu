s=input("enter ip ")
s=s.split(".")
if len(s)!=4:
    print("invalid")
else:
    if int(s[0])!=140 or int(s[1])!=138:
        print('140.138')
    else:
        if int(s[2])<0 or int(s[3])<0:
            print("0<s<255")
        elif int(s[2])>255 or int(s[3])>255:
            print("0<s<255")
        else:
            print("valid")