
def squares(n):
    curent_num = 1

    while curent_num <= n:
        yield curent_num**2
        curent_num +=1

print(list(squares(5)))