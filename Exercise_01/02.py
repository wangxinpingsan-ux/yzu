number=int(input("enter seconds:"))
day=number//86400
number-=(86400*day)
hour=number//3600
number-=(3600*hour)
minute=number//60
second=number%60

print(f"{day} day(s), {hour} hour(s), {minute} minute(s), and {second} second(s).")
