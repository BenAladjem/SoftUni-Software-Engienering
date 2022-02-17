tt = (1, 2, 3)

x, y, z = tt

def add(x, y, z):
    return x + y + z

numbers = (1, 2, 3)
a, b, c = numbers

#variant3
print(add(*numbers))

numbers_dict = {
    'x' : 1,
    'y' : 2,
    'z' : 3,
}

print(add(**numbers_dict))