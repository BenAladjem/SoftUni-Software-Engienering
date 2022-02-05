size = int(input())
matrix = []
hole1 = []
hole2 = []
#holes = []
flag_holes = False
food = 0
for i in range(size):
    row = [x for x in input()]
    matrix.append(row)
#print(matrix)
snake_position = []
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "S":
            snake_position.append(r)
            snake_position.append(c)
        if matrix[r][c] == "B":
            if flag_holes:
                hole2.append(r)
                hole2.append(c)
            else:
                hole1.append(r)
                hole1.append(c)
                flag_holes = True


        #print(r, c)


def holes(matr, hol1, hol2, cur_pos, s_pos):
    new_pos = []
    if cur_pos == hol1:
        matr[hol2[0]][hol2[1]] = "S"
        matr[hol1[0]][hol1[1]] = "."
        new_pos = hol2
    else:
        matr[hol1[0]][hol1[1]] = "S"
        matr[hol2[0]][hol2[1]] = "."
        new_pos = hol1
    matr[s_pos[0]][s_pos[1]] = '.'
    return[matr, new_pos]

def print_matrix(m):
    for i in m:
        print(''.join([str(x) for x in i]))


def moving(c, c_pos):
    mov_pos = []
    if c == "up":
        mov_pos.append(c_pos[0]-1)
        mov_pos.append(c_pos[1])
    elif c == "down":
        mov_pos.append(c_pos[0] + 1)
        mov_pos.append(c_pos[1])
    elif c == "left":
        mov_pos.append(c_pos[0])
        mov_pos.append(c_pos[1] - 1)
    elif c == "right":
        mov_pos.append(c_pos[0])
        mov_pos.append(c_pos[1] + 1)
    else:
        pass
    return mov_pos

def action(m, sn_pos,mov_pos):
    mm = m
    mm[sn_pos[0]][sn_pos[1]] = '.'
    mm[mov_pos[0]][mov_pos[1]] = 'S'
    return mm

#print(snake_position)
#print(hole1)
#print(hole2)
#print(print_matrix(matrix))
command = input()
while command:
    c = command
    moving_pos = moving(c,snake_position)
    if 0 <= moving_pos[0] < size and 0 <= moving_pos[1] < size:

        if moving_pos == hole1 or moving_pos == hole2:
            matrix = holes(matrix,hole1, hole2, moving_pos,snake_position)[0]
            snake_position = holes(matrix, hole1, hole2, moving_pos,snake_position)[1]
        else:
            if matrix[moving_pos[0]][moving_pos[1]] == '*':
                food += 1
            matrix = action(matrix, snake_position, moving_pos)
            snake_position = moving_pos

        if food >= 10:
            print("You won! You fed the snake.")
            break
        #print(c)
        #print_matrix(matrix)
    else:
        matrix[snake_position[0]][snake_position[1]] = '.'
        print("Game over!")
        break


    command = input()

print(f"Food eaten: {food}")
print_matrix(matrix)



