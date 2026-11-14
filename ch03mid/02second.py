s1=input("input s1 ")
s2=input("input s2 ")
s1_len=len(s1)
s2_len=len(s2)
s3=""
if s1_len>s2_len:
    for i in range(s2_len):
        s3+=s1[i]+s2[i]
    s3+=s1[s2_len:]+s2[s2_len:]
    print(s3)
else:
    for i in range(s1_len):
        s3+=s1[i]+s2[i]
    s3+=s1[s1_len:]+s2[s1_len:]
    print(s3)


