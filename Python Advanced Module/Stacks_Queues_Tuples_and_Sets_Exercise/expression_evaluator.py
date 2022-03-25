from  collections import deque

arithmetic_expresions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


characters = input().split()

numbers = deque()

for ch in characters:
    if ch in arithmetic_expresions:
        result = numbers.popleft()
        curent_expresion = arithmetic_expresions[ch]
        while numbers:
            number = numbers.popleft()
            result = curent_expresion(result,number)
    else:
        numbers.append(int(ch))
        result = numbers.popleft(characters)


print(result)
        #Da se dowyrchi !