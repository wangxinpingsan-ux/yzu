import string
s=string.whitespace+string.punctuation
n=input("enter sentence ")
for i in n :
    if i in s and i !=i:
        n=n.replace(i," ")

n=n.split()
if len(n)==0:
    print(0)
else:
    print(len(n[-1]))

