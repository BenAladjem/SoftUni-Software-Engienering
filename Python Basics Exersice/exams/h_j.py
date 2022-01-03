planned_jump = int(input())
first_jump = planned_jump-30
all_jumps = 0
flag = False
for i in range (first_jump,planned_jump+1,+5):
    fall_jump = 0
    for j in range(1,4):
        jump = int(input())
        all_jumps += 1
        if jump <= i:
            fall_jump +=1
        else:
            break
        if fall_jump ==3:
            flag = True
            print(f"Tihomir failed at {i}cm after {all_jumps} jumps.")
            break
    if flag:
        break
if jump> planned_jump:
    print(f"Tihomir succeeded, he jumped over {planned_jump}cm after {all_jumps} jumps.")
#Ok