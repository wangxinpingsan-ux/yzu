s=input("enter sentence ")
i=s.find("t")
if i==-1:
    print("none")
else:
    while i!=-1:
        print(i)
        i=s.find("t",i+1)
        

