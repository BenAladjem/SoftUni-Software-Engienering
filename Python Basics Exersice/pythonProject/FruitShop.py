type_fruit = input()
day_week = input()
volume = float(input())
price = 0

if type_fruit =='banana':
    if day_week =='Sunday' or day_week=='Saturday':
        price = volume*2.7
    elif day_week=='Monday'or day_week =='Tuesday'or day_week=='Wednesday'or day_week=='Thursday'or day_week=='Friday':
        price = volume*2.5
    else:
        price = 'error'

elif type_fruit == 'apple':
    if day_week == 'Sunday' or day_week=='Saturday':
        price = volume * 1.25
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume * 1.2
    else:
        price= 'error'

elif type_fruit =='orange':
    if day_week =='Sunday' or day_week=='Saturday':
        price = volume*0.9
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume*0.85
    else:
        price='error'

elif type_fruit =='grapefruit':
    if day_week =='Sunday' or day_week=='Saturday':
        price = volume*1.6
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume*1.45
    else:
        price='error'

elif type_fruit =='kiwi':
    if day_week =='Sunday' or day_week =='Saturday':
        price = volume*3.0
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume*2.7
    else:
        price='error'

elif type_fruit =='pineapple':
    if day_week =='Sunday' or day_week=='Saturday':
        price = volume*5.6
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume*5.5
    else:
        price = 'error'

elif type_fruit =='grapes':
    if day_week =='Sunday' or day_week== 'Saturday':
        price = volume*4.2
    elif day_week == 'Monday' or day_week == 'Tuesday' or day_week == 'Wednesday' or day_week == 'Thursday' or day_week == 'Friday':
        price = volume*3.85
    else:
        price='error'
else:
    price='error'
if type(price)==str:
    print('error')
else:
    print("{0:.2f}".format(price))