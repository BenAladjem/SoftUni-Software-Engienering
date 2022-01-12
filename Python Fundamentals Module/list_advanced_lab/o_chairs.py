num = int(input())
left = 0
flag = True
free_ch = 0
for i in range(num):
    command = input().split()
    ch = len(command[0])
    people = int(command[1])
    if people > ch:
        print(f"{people - ch} more chairs needed in room {i + 1}")
        flag = False
    else:
        free_ch += (ch - people)
if flag:
    print(f"Game On, {free_ch} free chairs left")

