word = input()
l = []
p = 0
for i in word:
    #if 64 < ord(i) <91:
    if i.isupper():
        l.append(p)
    p+=1
print(l)