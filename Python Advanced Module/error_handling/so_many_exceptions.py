numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif number <= 10:
        result /= number

print(result)

raise  TypeError('The type is incorrect')

class ValueTooSmallError(Exception):
    pass
raise ValueTooSmallError('The value is too small')

