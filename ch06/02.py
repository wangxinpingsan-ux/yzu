fout=open("C:\\yzu\\ch06\\golf.txt","w")
n=int(input("how many "))
for i in range(n):
    name=input("enter name ")
    print(name,file=fout)
    score=input("enter scorce ")
    print(score,file=fout)
fout.close()