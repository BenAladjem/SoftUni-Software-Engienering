word = input()
reversed_word = ''
l = len(word)
for i in range(l-1,-1,-1):
    reversed_word+=word[i]
print(reversed_word)

