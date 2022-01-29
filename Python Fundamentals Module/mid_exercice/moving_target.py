
targets_int = [int(x) for x in input().split()]
command = input()
while not command == "End":

    com = command.split()
    index = int(com[1])
    value = int(com[2])

    if com[0] == "Shoot":

        if 0 <= index < len(targets_int):
            targets_int[index] -= value
        if targets_int[index] <= 0:
            targets_int.pop(index)

    elif com[0] == "Add":
        if 0 <= index < len(targets_int):
        #if value in targets_int and (index >= 0):
            targets_int.insert(index,value)

        else:
            print("Invalid placement!")

    elif com[0] == "Strike":
        rad = value
        min = index - rad
        max = index + rad
        if max >= len(targets_int) or min < 0 or index < 0:
            print("Strike missed!")
        else:
            for i in range(rad*2 +1):
                targets_int.pop(min)
    #else:
        #break
    command = input()
    # if command == "End":
    #     break
# targets_int = [str(x) for x in targets_int]
# print("|".join(targets_int))

print(*targets_int, sep="|")