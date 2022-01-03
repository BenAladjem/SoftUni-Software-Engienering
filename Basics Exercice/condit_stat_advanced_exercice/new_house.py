type_flowers = input()
number_flovers = int(input())
budget = int(input())
price_per_flovers = 0
if type_flowers =="Roses":
    price_per_flovers = 5
    if number_flovers > 80:
        price_per_flovers *= 0.9
elif type_flowers == "Dahlias":
    price_per_flovers = 3.80
    if number_flovers > 90:
        price_per_flovers *= 0.85
elif type_flowers == "Tulips":
    price_per_flovers = 2.80
    if number_flovers > 80:
        price_per_flovers *= 0.85
elif type_flowers == "Narcissus":
    price_per_flovers = 3
    if number_flovers < 120:
        price_per_flovers *= 1.15
elif type_flowers == "Gladiolus":
    price_per_flovers = 2.50
    if number_flovers < 80:
        price_per_flovers *= 1.20
needed_money = number_flovers*price_per_flovers
delta = abs(budget-needed_money)
if budget >= needed_money:
    print(f"Hey, you have a great garden with {number_flovers} {type_flowers} and {delta:.2f} leva left.")
else:
    print(f"Not enough money, you need {delta:.2f} leva more.")