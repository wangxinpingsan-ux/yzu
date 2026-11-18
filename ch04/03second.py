import string
s=input("enter sentence ").lower()
ban=string.punctuation+string.whitespace
for i in s:
    if i in ban:
        s=s.replace(i,'')   
if s==s[::-1]:
    print("is palindrome")
else:
    print("is not palindrome")