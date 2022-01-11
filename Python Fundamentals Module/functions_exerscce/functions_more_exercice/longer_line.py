import math

x1 = input()
y1 = input()
x2 = input()
y2 = input()

a1 = input()
b1 = input()
a2 = input()
b2 = input()

x = (float(x1)-float(x2))
y = (float(y1)-float(y2))
hxy = math.sqrt(x*x + y*y)

a = (float(a1)-float(a2))
b = (float(b1)-float(b2))
hab = math.sqrt(a*a + b*b)

def closer(a,b,c,d):
    h1 = math.sqrt(float(a) * float(a) + float(b) * float(b))
    h2 = math.sqrt(float(c) * float(c) + float(d) * float(d))
    if h1 <= h2:
        print(f"({math.floor(float(a))}, {math.floor(float(b))})({math.floor(float(c))}, {math.floor(float(d))})")
    else:
        print(f"({math.floor(float(c))}, {math.floor(float(d))})({math.floor(float(a))}, {math.floor(float(b))})")

if hxy >= hab:
    closer(x1,y1,x2,y2)
else:
    closer(a1,b1,a2,b2)