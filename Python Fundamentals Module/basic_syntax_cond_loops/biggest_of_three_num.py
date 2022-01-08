list = []
for i in range(0,3):
    num = int(input())
    list.append(num)
list.sort(reverse=True)
print(list[0])