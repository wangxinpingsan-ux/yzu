try:
    with open("C:\\yzu\\ch06\\numbers.txt") as f:
        total=0
        count=0
        for i in f:
            try:
                i=int(i.strip())
                total+=i
                count+=1
            except ValueError:
                continue
        print(total/count)
except FileNotFoundError:
    print("invalid")

        