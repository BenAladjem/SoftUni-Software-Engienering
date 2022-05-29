n = int(input())

for i in range(n):
    spases = n - i - 1
    stars = i + 1
    line_spases = ''.join([' '] * spases)
    line_stars = ' '.join(['*'] * stars)
    print(line_spases + line_stars)

for i in range(n):
    spases = n - i - 1
    stars = i + 1