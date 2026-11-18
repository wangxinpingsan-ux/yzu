fin=open("C:\\Users\\wangx\\Downloads\\ch_06_files_and_exceptions\\ch_06_Files_and_Exceptions\\Dengue_Daily_last12m_EN.csv","r", newline="",encoding="windows-1252")
count=0
for line in fin:
    line=line.strip()
    
    i=line.split(",")
    
    if i[5]=="Taipei City"or i[5]=="New Taipei City":
        print(f"{i[0]} {i[3]} {i[4]:10} {i[5]:20} {i[6]:15}")
        count+=1
fin.close() 
print(count)