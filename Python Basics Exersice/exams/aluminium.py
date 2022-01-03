#import sys

joinery_count = int(input())
kind_joinery = input()
delivery = input()
total = 0

#if joinery_count < 10:
    #print('Invalid order',end='')
   # sys.exit(0)

if kind_joinery == '90X130':
    prise = 110
    prise *= joinery_count
    if joinery_count > 60:
        prise *= 0.92
    elif 30 < joinery_count:
        prise *= 0.95
    total = prise

elif kind_joinery == '100X150':
    prise = 140
    prise *= joinery_count
    if joinery_count > 80:
        prise *= 0.9
    elif 40 < joinery_count:
        prise *= 0.94
    total = prise

elif kind_joinery == '130X180':
    prise = 190
    prise *= joinery_count

    if joinery_count > 50:
        prise *= 0.88
    elif 20 < joinery_count:
        prise *= 0.93
    total = prise
elif kind_joinery == '200X300':
    prise = 250
    prise *= joinery_count

    if joinery_count > 50:
        prise *= 0.86
    elif 25 < joinery_count:
        prise *= 0.91
    total = prise

if delivery == "With delivery":
    total += 60

if joinery_count > 99:
    total *= 0.96
if joinery_count < 10:
    print('Invalid order')
else:
    print(f"{total:.2f} BGN")