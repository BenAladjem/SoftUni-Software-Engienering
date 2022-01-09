text = input().split()
products = input().split()
d_products = {}

for index in range(0,len(text), 2):
    items = text[index]
    qtt = text[index+1]
    d_products[items] = qtt
for product in products:
    if product in d_products:
        print(f"We have {d_products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
