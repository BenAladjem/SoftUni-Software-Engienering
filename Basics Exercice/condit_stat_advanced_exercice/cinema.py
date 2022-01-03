type_movie = input()
rows = int(input())
cols = int(input())
total_plases = rows*cols
price_tickets = 0
if type_movie == 'Premiere':
    price_tickets = 12
elif type_movie == 'Normal':
    price_tickets = 7.5
else:
    price_tickets = 5
total_income = total_plases*price_tickets
print(f"{total_income:.2f} leva")