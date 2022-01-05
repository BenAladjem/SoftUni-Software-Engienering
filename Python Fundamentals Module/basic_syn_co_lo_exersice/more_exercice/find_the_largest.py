number = input()
l = []
for i in number:
    l.append(i)
    l.sort(reverse=True)
for i in range(len(l)):
    print(l[i],end='')