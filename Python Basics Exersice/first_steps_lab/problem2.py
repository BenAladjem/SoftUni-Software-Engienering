numbers = [int(x) for x in input().split()]
#print(numbers)
command = input()
while not command == "Finish":
    action = command.split()
    value = int(action[1])
    if action[0] == "Add":
        numbers.append(value)
    elif action[0] == "Remove":
        numbers.remove(value)
    elif action[0] == "Replace":
        rep = int(action[2])
        i = numbers.index(value)
        numbers.pop(i)
        numbers.insert(i,rep)

    elif action[0] == "Collapse":
        numbers = [x for x in numbers if x >= value]


    command = input()
print(*numbers, sep=" ")