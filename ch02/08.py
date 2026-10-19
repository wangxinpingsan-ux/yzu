while True:
    width=int(input("enter width "))
    if width==0:
        break
    height=int(input("enter height "))
    if height==0:
        break
    if width<0 or height<0:
        print("invaild")
    else:
        print(width*height)

