energy = int(input())
command = input()
count = 0
flag = True
while not command == "End of battle":
    en = int(command)
    energy -= en
    count += 1
    if count%3 == 0 and energy >= 0:
        energy += count
    if energy < 0:
        count-=1
        energy+=en

        print(f"Not enough energy! Game ends with {count} won battles and {energy} energy")
        flag = False
        break

    command = input()
if flag:
    print(f"Won battles: {count}. Energy left: {energy}")