command = input()
sum = 0
flag = False
while not (command == 'regular' or command == 'special'):
    if float(command)<0:
        print("Invalid price!")
    else:
        sum += float(command)
    command = input()
    if command == 'special':
        flag = True
if sum == 0:
    print("Invalid order!")
else:
    total_sum = 1.2 * sum
    taxes = sum * 0.2
    if flag:
        total_sum = 0.9 * total_sum
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")

