def sum(num):
    if num <= 2:
        return 1
    return sum(num-1) + sum(num - 2)


print(sum(6))
