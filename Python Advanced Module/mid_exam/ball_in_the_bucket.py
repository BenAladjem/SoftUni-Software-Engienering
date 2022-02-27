matrix = []
for i in range(6):
    row = [x for x in input().split(' ')]
    matrix.append(row)
def sum_col(m, com):
    sum = 0
    for i in range(6):
        if not i == com[0]:
            sum += int(m[i][com[1]])
        else:
            pass
    return sum


count = 0
for i in range(3):
    y = input()
    y = y[1:-1]
    com = [int(x) for x in y.split(', ')]
    #print(com)
    if 0 <= com[0] < 6 and 0 <= com[1] < 6:
        if matrix[com[0]][com[1]] == "B":
            count += sum_col(matrix, com)
            matrix[com[0]][com[1]] = "0"
#print(count)
if count < 100:
    print(f"Sorry! You need {100 - count} points more to win a prize.")
elif count < 200:
    print(f"Good job! You scored {count} points, and you've won Football.")
elif count <300:
    print(f"Good job! You scored {count} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {count} points, and you've won Lego Construction Set.")
