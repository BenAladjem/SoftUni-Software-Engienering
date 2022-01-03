planned_jump = int(input())
first_jump = planned_jump-35
all_jumps = 0
fall_jump = 0
jump = 0
flag = False
i = 0
#for i in range (first_jump,planned_jump+1,+5):
while flag == False and first_jump<planned_jump:
    first_jump+=5
    fall_jump = 0
    jump = int(input())
    all_jumps+=1
    if jump > planned_jump:
        print(f"Tihomir succeeded, he jumped over {planned_jump}cm after {fall_jump + all_jumps} jumps.")
        break
    if jump <= first_jump:
        while jump<=first_jump and fall_jump <3:
            fall_jump+=1

            if fall_jump ==3:
                flag = True
                print(f"Tihomir failed at {first_jump}cm after {all_jumps} jumps.")
                break
            else:
                jump = int(input())
                all_jumps += 1

        if flag:
            break


