days = int(input())
type_room = input()
rating = input()
nights = days - 1
sum = 0
if type_room == 'room for one person':
    sum = nights*18
elif type_room == 'apartment':
    if days < 10:
        sum = nights*25.00*0.7
    elif days < 15:
        sum = nights*25 * 0.65
    else:
        sum = nights*25*0.5
else:
    if days < 10:
        sum = nights*35.00*0.9
    elif days < 15:
        sum = nights*35 * 0.85
    else:
        sum = nights*35*0.8
if rating == 'positive':
    sum*=1.25
else:
    sum*=0.9
print("{0:.2f}".format(sum))