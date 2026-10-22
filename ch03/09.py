import string
s = input('give a string: ')
s = s.strip(string.punctuation)
print(s)
lst = s.split(' ')

print(len(lst[-1]))