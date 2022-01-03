budget = int(input())
season = input()
num_fishmans = int(input())
boat_rent = 0
if season=='Spring':
    boat_rent = 3000
elif season =="Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if num_fishmans <= 6:
    boat_rent*=0.9
elif num_fishmans <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if season != "Autumn" and num_fishmans%2==0:
    boat_rent *= 0.95
delta = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {delta:.2f} leva left.")
else:
    print(f"Not enough money! You need {delta:.2f} leva.")



