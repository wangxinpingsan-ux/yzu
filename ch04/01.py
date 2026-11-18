s = input("input sentence ")
l = len(s)
n = s.find("t")
while n!=-1:
        print(n)
        n = s.find("t", n + 1)
