#kom
product = input()
town = input()
num = float(input())

result = 0
if town =='Sofia':
    if product == 'coffee':
        result = num*0.50
    elif product == 'water':
        result = num*0.8
    elif product == 'beer':
        result = num*1.20
    elif product == 'sweets':
        result = num * 1.45
    else:
        result = num * 1.60
elif town == 'Varna':
    if product == 'coffee':
        result = num * 0.45
    elif product == 'water':
        result = num * 0.7
    elif product == 'beer':
        result = num * 1.10
    elif product == 'sweets':
        result = num * 1.35
    else:
        result = num * 1.55
else:
    if product == 'coffee':
        result = num * 0.4
    elif product == 'water':
        result = num * 0.7
    elif product == 'beer':
        result = num * 1.15
    elif product == 'sweets':
        result = num * 1.30
    else:
        result = num * 1.50

print(result)
