text = input()
num_beggars = int(input())
l = text.split(", ")
intl = []
result_l = []

lend = len(l)
for i in l:
    intl.append(int(i))
for j in range(num_beggars):
    num = j
    result = 0
    while num < lend:
        result +=intl[num]
        num +=num_beggars
    result_l.append(result)
print(result_l)