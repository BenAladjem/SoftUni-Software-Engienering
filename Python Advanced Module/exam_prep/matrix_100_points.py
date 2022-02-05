import math
from sys import stdin
#
# input1 = '''5
# 1 X 7 9 11
# X 14 46 62 0
# 15 33 21 95 X
# P 14 3 4 18
# 9 20 33 X 0
# right
# right
# up
# up
# left
# down'''
# input2 = '''8
# 13 18 9 7 24 41 52 11
# 54 21 19 X 6 4 75 6
# 76 5 7 1 76 27 2 37
# 92 3 25 37 52 X 56 72
# 15 X 1 45 45 X 7 63
# 1 63 P 2 X 43 5 1
# 48 19 35 20 100 27 42 80
# 73 88 78 33 37 52 X 22
# up
# left'''

#n = int(input())


#class StringIO(object):
    #pass


#stdin = StringIO(input1)
#stdin = StringIO(input2)
n = int(input())
matrix = []
win_pos = []
flag = True
for i in range(n):
    row = [x for x in input().split(' ')]
    matrix.append(row)

def p_position(mat):
    p_pos = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "P":
                p_pos.append(i)
                p_pos.append(j)
    return p_pos
#print(p_position(matrix))

def action(command, matr, curent_pos):
    new_pos = []
    if command == "up":
        new_pos = matr[curent_pos[0]-1][curent_pos[1]]
    elif command == "down":
        new_pos = matr[curent_pos[0]+1][curent_pos[1]]
    elif command == "left":
        new_pos = matr[curent_pos[0]][curent_pos[1]-1]
    elif command == "right":
        new_pos = matr[curent_pos[0]][curent_pos[1]+1]
    #com_pos =matr[new_pos[0]][new_pos[1]]
    return new_pos
def pos(command, matr, curent_pos):
    pos = []
    if command == "up":
        pos.append(curent_pos[0]-1)
        pos.append(curent_pos[1])
    elif command == "down":
        pos.append(curent_pos[0]+1)
        pos.append(curent_pos[1])
    elif command == "left":
        pos.append(curent_pos[0])
        pos.append(curent_pos[1]-1)
    elif command == "right":
        pos.append(curent_pos[0])
        pos.append(curent_pos[1]+1)
    return pos

#com = input()
cur_pos = []
for el in p_position(matrix):
    cur_pos.append(el)
sum_poits = 0
while True:
    com:str = input()
    valid_com = ['up', 'down', 'left', 'right']

    if com in valid_com:
        next_p = action(com, matrix, cur_pos)
        cur_pos = pos(com, matrix, cur_pos)

        if next_p == 'X' or (cur_pos[0]<0) or cur_pos[0]>=n \
            or cur_pos[1]<0 or cur_pos[1]>n:
            sum_poits = sum_poits//2
            print(f"Game over! You've collected {sum_poits} coins.")
            flag = False
            break
        else:
            sum_poits += int(next_p)
            win_pos.append(cur_pos)
        #print(sum_poits, win_pos)
    else:
        pass
    #com = input()
    if not com:
        break
if flag:
    print(f"You won! You've collected {sum_poits} coins.")
print("Your path:")
for el in win_pos:
    print(el)




