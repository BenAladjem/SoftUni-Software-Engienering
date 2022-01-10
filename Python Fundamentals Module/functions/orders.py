type = input()
quantity = int(input())
product = 0
if type =="coffee":
    product =1.50
elif type == "water":
    product = 1.00
elif type =="coke":
    product = 1.40
elif type == "snacks":
    product = 2.00
def order (p,q):
    return p*q
print("%.2f"%order(product,quantity))