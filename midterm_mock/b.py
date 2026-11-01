while True:
    n=int(input("enter n "))
    if n==0:
        break
    elif n<0:
        print("invalid")
        continue
    else:
        ans=[]
        while n>=10:
            ans.append(n%10)
            n//=10
        ans.append(n)
    palindrome=True
    for i in range(len(ans)):
        x=len(ans)-i
        if ans[i]!=ans[x-1]:
            palindrome=False
            break
    print("reverse: ",end="")
    for k in range(len(ans)):
        print(ans[k],end='')
    print()
    if palindrome:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


