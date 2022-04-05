import sys
from io import StringIO

test_input = '''1
1
2
3
4
5'''

sys.stdin = StringIO(test_input)

def get_player_choice(player):
    choice = input(f'Player {player}, please choose a column\n')
    return choice

def apply_player_choice():
    row_index = 0



def check_win_condition(board, row_index, column_index, win_count):
    pass
    right_win_condition = [r for r in range(row_index, row_index + win_count)]
    left_win_condition = None
    up_win_condition = None
    down_win_condition = None

    up_left_condition = None
    up_right_condition = None
    down_left_condition = None
    down_right_condition = None

def play(board):
    pass

def create_board(rows_count, columns_count):
    return [[None]*columns_count for _ in range(rows_count)]

def print_board(board):
    def get_value(value):
        if value is None:
            return 0
        return value

    for row in board:
        print([get_value(x) for x in row])
#board = []
board = create_board(6, 7)
play(board)