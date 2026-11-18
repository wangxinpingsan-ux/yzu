s=input("input sentence ")
lst=s.split()
if len(lst) >= 2:
    print(lst[1])
else:
    print("invalid")