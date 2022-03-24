n = int(input())

def fuck(num):
    if num == 0:
        return 1
    return num*fuck(num-1)
print(fuck(n))