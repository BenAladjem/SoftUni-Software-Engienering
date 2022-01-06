text = input()
counter = 0
for sym in text:
    if sym == 'a':
        counter += 1
    elif sym == 'e':
        counter += 2
    elif sym == 'i':
        counter += 3
    elif sym == 'o':
        counter += 4
    elif sym == 'u':
        counter += 5

print(counter)
