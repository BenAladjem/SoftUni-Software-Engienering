budget = float(input())
season = input()
price = 0
where = "Hotel"
if budget <= 100:
    print("Somewhere in Bulgaria")
    if season=="summer":
        price =0.3*budget
        where = "Camp"
    else:
        price = 0.7*budget
elif budget >1000:
    print("Somewhere in Europe")
    price = 0.9*budget
else:
    print("Somewhere in Balkans")
    if season =="summer":
        price  = 0.4*budget
        where = "Camp"
    else:
        price = 0.8*budget
print(f"{where} - {price:.2f}")
