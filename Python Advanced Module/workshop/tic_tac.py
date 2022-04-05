from pip._vendor.colorama import Fore


def read_players_info():
    player_one_name = ''
    player_two_name = ''
    while player_one_name == '':
        player_one_name = input('Player one name: ')
    while player_two_name == '' or player_two_name == player_one_name:
        if player_two_name == '':
            player_two_name = input('Player two name: ')
        else:
            player_two_name = input('Please enter different name: ')


    player_one_sign = input(f'{player_one_name}, would you like to play with "X" or "O"?')
    while not player_one_sign in ['X', 'O']:
        print('Please enter olny "X" or "O"!')
        player_one_sign = input()
    player_two_sign = "O" if player_one_sign == "X" else "X"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    return [player_one, player_two]

def print_board_numeration():
    print('This is the numeration of the board:')
    print('|  1  |  2  |  3  |')
    print('|  4  |  5  |  6  |')
    print('|  7  |  8  |  9  |')

def command_position(com):
    position = []
    if com == "1":
        position = [0, 0]
    elif com == "2":
        position = [0, 1]
    elif com == "3":
        position = [0, 2]
    elif com == "4":
        position = [1, 0]
    elif com == "5":
        position = [1, 1]
    elif com == "6":
        position = [1, 2]
    elif com == "7":
        position = [2, 0]
    elif com == "8":
        position = [2, 1]
    elif com == "9":
        position = [2, 2]
    return position

def draw_matrix(matrix):
    for row in matrix:
        print('|  ', end='')
        print('  |  '.join([str(x) for x in row]), end='')
        print('  |')

matrix = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']
          ]

# matrix = [['1', '2', '3'],
#           ['4', '5', '6'],
#           ['7', '8', '9']
#           ]

def play(name, sign, matr):
    player = name
    sig = sign
    command = input(f'{player}, choose a free position[1 - 9]: ')
    while not command in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Please enter number [1 - 9]')
        command = input()

    while command in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and\
            matrix[command_position(command)[0]][command_position(command)[1]] != ' ':
        print("Please enter free position!")
        command = input()
    a = int(command_position(command)[0])
    b = int(command_position(command)[1])
    matr[a][b] = sig
    return matr

def win_check(sign, matr):
    flag = False
    if         ((matr[0][0] == matr[0][1] == matr[0][2])) and not matr[0][0] ==' '\
            or ((matr[1][0] == matr[1][1] == matr[1][2])) and not matr[1][0] ==' '\
            or ((matr[2][0] == matr[2][1] == matr[2][2])) and not matr[2][0] ==' '\
            or ((matr[0][0] == matr[1][0] == matr[2][0])) and not matr[0][0] ==' '\
            or ((matr[0][1] == matr[1][1] == matr[2][1])) and not matr[0][1] ==' '\
            or ((matr[0][2] == matr[1][2] == matr[2][2])) and not matr[0][2] ==' '\
            or ((matr[0][0] == matr[1][1] == matr[2][2])) and not matr[0][0] ==' '\
            or ((matr[0][2] == matr[1][1] == matr[2][0])) and not matr[0][2] ==' ':
        flag = True
    return flag
    # [0, 0], [0, 1], [0, 2]
    #[1, 0], [1, 1], [1, 2]
    #[2, 0], [2, 1], [2, 2]

    # [0, 0], [1, 0], [2, 0]
    # [0, 1], [1, 1], [2, 1]
    # [0, 2], [1, 2], [2, 2]

    #[0, 0], [1, 1], [2, 2]
    #[0, 2], [2, 2], [2, 0]

player_one, player_two = read_players_info()
player_one_name = player_one[0]
player_one_sign = player_one[1]
player_two_name = player_two[0]
player_two_sign = player_two[1]
print_board_numeration()
print(f'{player_one[0]} starts first!')

count_turns = 0
flag_win = False
while count_turns < 9 or not flag_win:
    count_turns +=1
    if count_turns % 2 == 0:
        turn_name = player_two_name
        turn_sign = player_two_sign
    else:
        turn_name = player_one_name
        turn_sign = player_one_sign
    matrix = play(turn_name, turn_sign, matrix)

    draw_matrix(matrix)
    #print(turn_sign)
    if win_check(turn_sign,matrix):
        print(Fore.RED+f'{turn_name} win!')
        flag_win = True
        break
    if count_turns == 9:
        print('There is no winner')
        break

