def read_first_player_sign(first_player_name):
    while True:
        first_player_sign = input(f'{first_player_name} would you like to play with X or )? ')
        if first_player_sign in['X', 'O']:
            return first_player_sign

def play(matrix, p1 , p2):
    #
    turn = 1
    players_turns = {0:p2, 1:p1}
    while True:
        #find wich player turn is
        name, sign = [turn % 2]
        #read position
        #play position
        pass


def read_players_info():
    first_player_name = input('Player one name: ')
    second_player_name = input('Player two name: ')

    first_player_sign = read_first_player_sign(first_player_name)
    second_player_sign = 'O' if first_player_sign == 'X' else 'X'
    return [first_player_name, first_player_sign], [second_player_name, second_player_sign]


def print_board_numeration():
    print('This is the numeration of the board:')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')


player1, player2 = read_players_info()

read_players_info()

