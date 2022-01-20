text = [x for x in input()]
l = len(text)
lis = []
for i in range(l-1):
    if text[i]==text[i+1]:
        lis.append(i)
#print(lis)
lis = lis[::-1]

for j in lis:
    text.pop(j)
print("".join(text))