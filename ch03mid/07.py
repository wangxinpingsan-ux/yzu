import string

s = input("input ")
if s.isalpha():
    print("alphabetic")
elif s.isdecimal():
    print("decimal")
else:
    ishex = True
    for i in s:
        if i not in string.hexdigits:
            ishex = False
            break
    if ishex:
        print("hexadecimal")
    else:
        print("none")
