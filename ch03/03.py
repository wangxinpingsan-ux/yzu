s=input("enter string ")
count=0
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i!=j and i!=k and j!=k:
                print(s[i]+s[j]+s[k])

                count+=1
print(f"The total number of permutations is {count}")