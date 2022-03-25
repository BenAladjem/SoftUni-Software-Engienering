first = set([int(x) for x in input().split()])
second = set(int(x) for x in input().split())

n = int(input())

for _ in range (n):
    line_args = input().split()
    command = line_args[0]
    command_parametur = line_args[1]

    if command == 'Add' and command_parametur == 'First':
        [first.add(int(x)) for x in line_args[2:]]
    elif command == 'Ádd' and command_parametur == 'Second':
        [second.add(int(x)) for x in line_args[2:]]
    elif command == 'Remove' and command_parametur == 'Second':
        pass

    #da se dowurchi
