target = int(input())
start_jump = target - 30
total_jumps = 0
jump_height = 0
list_ok = []
list_ok1 = []
list_off = []
list_off1 =[]
all_list =[]
while  start_jump <= target:
    failed_jumps = 0
    for i in range(1,4):
        jump_height = int(input())

        total_jumps += 1

        if jump_height > target:
            print(f"Tihomir succeeded, he jumped over {target}cm after {total_jumps} jumps.")
            break
        elif jump_height > start_jump:
            list_ok1.append(start_jump)
            list_ok.append(jump_height)
            start_jump +=5
            break
        else:
            failed_jumps +=1
            list_off1.append(start_jump)
            list_off.append(jump_height)
    if failed_jumps == 3:
        print(f"Tihomir failed at {start_jump}cm after {total_jumps} jumps.")
        break
    if jump_height > target:
        break
print(list_ok1)
print(list_ok)
print(list_off1)
print(list_off)