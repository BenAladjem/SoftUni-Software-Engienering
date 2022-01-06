town = input()
s = float(input())
volume = 'error'

if town == 'Sofia':
    if s > 10000:
        volume = s * 12 / 100
    elif s > 1000:
        volume = s * 8 / 100
    elif s > 500:
        volume = s * 7 / 100
    elif s > 0:
        volume = s * 5 / 100
    else:
        volume = 'error'

elif town == 'Varna':
    if s > 10000:
        volume = s * 13 / 100
    elif s > 1000:
        volume = s * 10 / 100
    elif s > 500:
        volume = s * 7.5 / 100
    elif s > 0:
        volume = s * 4.5 / 100
    else:
        volume = 'error'

elif town == 'Plovdiv':
    if s > 10000:
        volume = s * 14.5 / 100
    elif s > 1000:
        volume = s * 12 / 100
    elif s > 500:
        volume = s * 8 / 100
    elif s > 0:
        volume = s * 5.5 / 100
    else:
        volume = 'error'
#else:
 #   volume = 'error'

if type(volume) == str:
    print('error')
else:
    print("{0:.2f}".format(volume))
