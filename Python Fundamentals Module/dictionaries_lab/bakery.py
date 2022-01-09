text = input().split()
#print(text)
products = {}
for i in range(0,len(text),2):
    key = text[i]
    value = int(text[i+1])
    products[key] = value
print(products)