num = [int(input()) for _ in range(5)]


class ValueCannotBeNegative:
    pass

try:
    for n in num:
        if n < 0:
            raise ValueCannotBeNegative
    print('No exception')
except:
    print('Exception handelned')

print('End')