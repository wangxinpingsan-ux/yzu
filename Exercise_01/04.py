price=int(input("enter price(<100)"))
price=100-price
c50=price//50
price%=50
c10=price//10
price%=10
c5=price//5
c1=price%5
print(f"50:{c50}\n10:{c10}\n5:{c5}\n1:{c1}")