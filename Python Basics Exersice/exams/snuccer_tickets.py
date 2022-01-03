phase_of_the_tournament = input()
ticket_type = input()
ticket_number = int(input())
picture_with_throphy = input()

ticket_price = 0
picture_price = 40

if phase_of_the_tournament == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif phase_of_the_tournament == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif phase_of_the_tournament == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400

total_price = ticket_price * ticket_number
total_picture_price = ticket_number * picture_price

if picture_with_throphy == "Y":
    if total_price > 4000:
        total_picture_price = 0
else:
    total_picture_price = 0
if 2500 < total_price <= 4000 :
    total_price = total_price * 0.9 + total_picture_price
elif total_price > 4000:
        total_price = total_price * 0.75 + total_picture_price
else:
    total_price = total_price +total_picture_price
print(f"{total_price:.2f}")