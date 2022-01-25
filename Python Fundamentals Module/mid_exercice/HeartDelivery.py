neighborhood = [int(num) for num in input().split("@")]
command = input()
position = 0
while not command == "Love!":
    length_jump = command.split()[1]
    length_jump = int(length_jump)


    if position + length_jump >= len():
        position = 0

    command = input()
