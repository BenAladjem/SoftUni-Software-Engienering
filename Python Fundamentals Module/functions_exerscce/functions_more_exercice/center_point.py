import math

a = input()
b = input()
c = input()
d = input()

h1 = math.sqrt(float(a)*float(a) + float(b)*float(b))
h2 = math.sqrt(float(c)*float(c) + float(d)*float(d))
if h1 <= h2:
    print(f"({math.floor(float(a))}, {math.floor(float(b))})")
else:
    print(f"({math.floor(float(c))}, {math.floor(float(d))})")