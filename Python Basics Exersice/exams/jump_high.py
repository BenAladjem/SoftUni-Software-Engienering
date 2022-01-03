target = int(input())
start_jump = target - 30
total_jumps = 0
failed_jumps = 0
while  start_jump <= target:
    jump_height = int(input())
    total_jumps += 1
    if jump_height > start_jump:
        start_jump +=5
        failed_jumps = 0
    else:
        failed_jumps +=1
    if failed_jumps == 3:
        print(f"Tihomir failed at {start_jump}cm after {total_jumps} jumps.")
        break
else:
    print(f"Tihomir succeeded, he jumped over {target}cm after {total_jumps} jumps.")


