import re
items = []
sum = 0
pattern = r'^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d*)!(?P<quantity>\d+)'
command = input()
while not command == "Purchase":
    match = re.match(pattern, command)
    if match is not None:
        name = match.group("furniture_name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        sum += price*quantity
        items.append(name)

    command = input()
print("Bought furniture:")
for n in items:
    print(n)
print(f"Total money spend: {sum:.2f}")

