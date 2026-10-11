num=int(input("enter five digit "))
d5=num%10
num//=10
d4=num%10
num//=10
d3=num%10
num//=10
d2=num%10
num//=10
d1=num
if d5==d1 and d4==d2:
    print("it's a palindrome")
else:
    print("it's not a palindrome")