a = [2, 4, 6, 8, 3, 5, 7, 9]
#print(sorted(a, reverse=True), end='?')

my_dict = {'Peter':21, 'George': 18, 'John':45, 'Adelle': 21}
print(sorted(my_dict.items(), key=lambda x: (x[1], x[0])))

print({key for key in my_dict.items()})

b = [0,1,2,3,4,5,6,7,8,9,10]
print(b[-4:])
print(b[4:2])