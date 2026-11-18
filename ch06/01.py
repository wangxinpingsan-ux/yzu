fin=open("C:\\yzu\\ch06\\numbers.txt","r")
total=0
count=0
for i in fin:
    i=i.strip()
    total+=int(i)
    count+=1
fin.close()
print(total/count)
