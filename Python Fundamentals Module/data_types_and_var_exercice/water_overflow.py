tank_vol = 255
vol = 0
n = int(input())
for i in range(n):
    l = int(input())
    vol += l
    if tank_vol < vol:
        print("Insufficient capacity!")
        vol -=l
print(vol)