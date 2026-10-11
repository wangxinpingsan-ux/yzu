terms=0
s=1
n=1
pi=0

while True:
    pi+=(4/n)*s
    n+=2
    s*=-1
    terms+=1
    if round(pi,4)==3.1415:
        print(terms)
        break

