male=int(input("enter number of male "))
female=int(input("enter number of female "))
total=male+female
percent_male=(male/total)*100
percent_female=(female/total)*100
int_percent_male=int(percent_male+0.5)
int_percent_female=int(percent_female+0.5)
print(f"Percent males: {int_percent_male}%\nPercent females: {int(int_percent_female)}%")