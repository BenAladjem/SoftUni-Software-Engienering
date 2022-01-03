budget = float(input())
category = input()
count_people = int(input())
transport = 0.0
price_ticket = 0.0
total_price = 0.0
all_expenses = 0.0
if 1 <= count_people <= 4:
    transport = budget * 0.25
elif count_people < 10:
    transport = budget * 0.40
elif count_people < 25:
    transport = budget * 0.50
elif count_people < 50:
    transport = budget * 0.60
else:
    transport = budget * 0.75
if category == "VIP":
    price_ticket = 499.99
else:
    price_ticket = 249.99
total_price = price_ticket * count_people
left_money = abs(total_price - transport)
all_expenses = total_price + transport
if all_expenses <= budget:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")