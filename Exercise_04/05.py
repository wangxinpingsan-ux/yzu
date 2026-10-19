i=1
count=0
while i <=999:

    d3=i//100
    d1=i%10
    if d3==d1:
        print(i,end=" ")
        count+=1
    i+=1


print(f"{count} palindromes")
                
