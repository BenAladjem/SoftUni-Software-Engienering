target = float(input())
command = input()
total_sum = 0
n_sum = 0
while command != "Party!":

    coctail = command
    num = int(input())
    l = len(command)
    n_sum += l * num
    if not n_sum % 2 == 0:
        n_sum *= 0.75
    total_sum += n_sum
    if total_sum >= target:
        print("Target acquired.")
        break
    n_sum = 0
    command = input()
    if command == "Party!":
        print(f"We need {(target - total_sum):.2f} leva more.")

print(f"Club income - {total_sum:.2f} leva.")
