name = input()
sum = 0
count_low = 0
count_grade = 0
for i in range(1,13):
    flag = True
    grad = float(input())
    count_grade+=1
    sum+=grad
    if grad<4:
        count_low+=1
    else:
        count_low = 0
    if count_low ==2:
        print(f"{name} has been excluded at {count_grade-1} grade")
        flag = False
        break
if flag:
    print(f"{name} graduated. Average grade: {(sum/12):.2f}")



