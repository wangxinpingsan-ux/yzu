import string
s=input("enter ")
ban=string.punctuation
for i in s:
    if i in ban:
        if i == "-":
            continue
        else:
            s=s.replace(i," ")
s=s.split()
if len(s)==0:
    print("0")
else:
    print(len(s[-1]))
