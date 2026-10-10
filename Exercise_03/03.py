pi = 0
terms = 1
n = 1
s=1
while True:

    pi = (4 / n)*s + pi
    s*=-1
    n +=2
    terms += 1
    if round(pi,3)==3.141:
        break
print(terms)
