num = int(input())
#query = ''
sta = []
for _ in range (num):
    query = input().split()

    if query[0] =='1':
        number = int(query[1])
        sta.append(number)
    elif query[0] == '2':
        if sta:
            sta.pop(-1)
    elif query[0] == '3':
        if sta:
            print(max(sta))
    elif query[0] == '4':
        if sta:
            print(min(sta))

res = []
while sta:
    res.append(str(sta.pop()))
print(', '.join(res))
