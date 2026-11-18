import csv
with open ("C:\\Users\\wangx\\Downloads\\ch_06_files_and_exceptions\\ch_06_Files_and_Exceptions\\Dengue_Daily_last12m_EN.csv",encoding="windows-1252", newline="") as f:
    readcsv=csv.reader(f)
    count=0
    for i in readcsv:
        if i[5]=="Taipei City"or i[5]=="New Taipei City":
            print(f"{i[0]} {i[3]} {i[4]:10} {i[5]:20} {i[6]:15}")
            count+=1
print(count)