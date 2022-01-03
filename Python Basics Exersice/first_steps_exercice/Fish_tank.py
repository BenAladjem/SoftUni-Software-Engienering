l = int(input())
w = int(input())
h = int(input())
busy_vol = float(input())

vol = l*w*h/1000
needed_vol = vol*(100-busy_vol)/100
print(needed_vol)
