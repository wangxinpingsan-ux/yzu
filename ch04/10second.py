s=list(input("enter "))
i=0
j=len(s)-1
while i<j:
    while i<j and s[i].isalpha()==False :
        i+=1
    while i<j and s[j].isalpha()==False:
        j-=1
    s[i],s[j]=s[j],s[i]
    i+=1
    j-=1
print("".join(s))
 
