text1 = input().split(", ")
text2 = input().split(", ")
result = []

for x in text1:
    for y in text2:
        if (x in y) and (not x in result):
            result.append(x)

print(result)
