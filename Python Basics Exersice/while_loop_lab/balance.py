command = input()
sum = 0
while command != "NoMoreMoney":
    num = float(command)

    if num > 0:
        sum += num
        print(f"Increase: {num:.2f}")
    else:
        print("Invalid operation!")

        break
    command = input()
print(f"Total: {sum:.2f}")

