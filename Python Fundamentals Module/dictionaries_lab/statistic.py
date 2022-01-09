text = input()
dict = {}

while not text == "statistics":
    text = text.split(":")
    product = text[0]
    qtt = int(text[1])
    if product in dict:
        dict[product]+=qtt
    else:
        dict[product] = qtt

    text = input()
print("Products in stock:")
for (product, qtt) in dict.items():
    print(f"{product}: {qtt}")
print(f"Total Products: {len(dict.keys())}")
print(f"Total Quantity: {sum(dict.values())}")
