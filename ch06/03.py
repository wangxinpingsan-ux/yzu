fin=open("C:\\yzu\\ch06\\golf.txt","r")
fout=open("C:\\yzu\\ch06\\golf2.txt","w")
for index,i in enumerate(fin):
    i=i.strip()
    if index%2==0:
        print(f"name: {i}",file=fout)
    else:
        print(f"score: {i}",file=fout)
fin.close()
fout.close()