num=int(input("enter five digit number "))
d1=num%10
num=num//10
d2=num%10
num=num//10
d3=num%10
num=num//10
d4=num%10
num=num//10
d5=num%10
if d1==d5 and d2==d4:
    print("palindrome")
