from pip._vendor.colorama import Fore


def sign():
    while True:
        first_player = input(Fore.RED +'First:')
        if first_player in ['X', 'Y', 'Z']:
            return first_player
        else:
            print('Only "X", "Y" or "Z"')


print(sign())