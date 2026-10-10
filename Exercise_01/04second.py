price=int(input("enter price (<100) "))
price=100-price
c50=price//50
price-=c50*50
c10=price//10
price-=c10*10
c5=price//5
price-=c5*5
c1=price
print(f"50: {c50}\n10: {c10}\n5: {c5}\n1: {c1}")

