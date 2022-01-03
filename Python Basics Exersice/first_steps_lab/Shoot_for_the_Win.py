target = [int(x) for x in input().split()]
#print(target)
command = input()
count = 0
index = 0
while not command == "End":
    index = int(command)
    if 0 <= index < len(target):
        x = target[index]
        for i in range(len(target)) :

            if target[i] > x and not target[i] == -1 and not i == index:
                target[i] -= x
            elif target[i] <= x and not target[i] == -1 and not i == index:
                target[i] += x
            elif not target[i] == -1 and target[i] == x and i == index:
                target[i] = -1
                count +=1

    command = input()
print(f"Shot targets: {count} -> ",end='')
print(*target, sep=" ")