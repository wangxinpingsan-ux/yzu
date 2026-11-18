import string
s=string.whitespace+string.punctuation
n=input("enter sentence ")
for i in n:
    print(i)
    if i in s:
        n=n.replace(i,"")

if n.lower()==n.lower()[::-1]:
    print("is palindrome")
else:
    print("is not palindrome")
