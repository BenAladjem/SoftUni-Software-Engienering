month = input()
num_nights = int(input())
price_app = 0
price_studio = 0
if month == "May" or month == "October":
    price_studio = 50
    price_app = 65
    if num_nights > 14:
        price_studio*=0.7
    elif num_nights > 7:
        price_studio *=0.95
elif month =="June" or month == "September":
    price_studio = 75.20
    price_app = 68.70
    if num_nights > 14:
        price_studio *= 0.8
else:
    price_studio = 76
    price_app = 77
if num_nights >14:
    price_app *= 0.9
print(f"Apartment: {num_nights*price_app:.2f} lv.")
print(f"Studio: {num_nights*price_studio:.2f} lv.")