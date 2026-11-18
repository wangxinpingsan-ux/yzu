s1=input("enter s1 ")
s2=input("enter s2 ")
s1_len=len(s1)
s2_len=len(s2)
s3=""
for i in range(min(s1_len,s2_len)):
    s3+=s1[i]+s2[i]
if s1_len>s2_len:
    s3+=s1[min(s1_len,s2_len):]
elif s1_len<s2_len:
    s3+=s2[min(s1_len,s2_len):]
print(s3)