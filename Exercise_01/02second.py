second=int(input("enter second "))
day=second//86400
second-=day*86400
hour=second//3600
second-=hour*3600
minute=second//60
second-=minute*60
print(f"{day} day ,{hour} hour ,{minute} minute ,{second} second ")

