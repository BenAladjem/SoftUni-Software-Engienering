text = input().split('|')
#print(text)
text = text[::-1]
result = []
for i in range(len(text)):
    t = text[i].split()
    result.append(t)

#print(result)

xx = []
for i in range(len(result)):
    x = result[i]
    for j in x:
        xx.append(j)

print(' '.join(xx))

