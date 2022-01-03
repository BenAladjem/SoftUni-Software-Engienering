temp = int(input())
time = input()
if time =="Morning":
    if 10<=temp<=18:
        o="Sweatshirt"
        sh = "Sneakers"
    elif 18<temp<=24:
        o = "Shirt"
        sh = "Moccasins"
    elif temp>=25:
        o = "T-Shirt"
        sh = "Sandals"
elif time=="Afternoon":
    if 10<=temp<=18:
        o="Shirt"
        sh = "Moccasins"
    elif 18<temp<=24:
        o = "T-Shirt"
        sh = "Sandals"
    elif temp>=25:
        o = "Swim Suit"
        sh = "Barefoot"

else:
    if 10<=temp<=18:
        o="Shirt"
        sh = "Moccasins"
    elif 18<temp<=24:
        o = "Shirt"
        sh = "Moccasins"
    elif temp>=25:
        o = "Shirt"
        sh = "Moccasins"
print(f"It's {temp} degrees, get your {o} and {sh}.")
