text1 = input().split(", ")
text2 = input()
result = [a for a in text1 if a in text2]

print(result)