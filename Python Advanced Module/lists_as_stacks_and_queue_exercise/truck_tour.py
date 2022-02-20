num = int(input())

station = []
for _ in range(num):
    x = input().split()
    x = [int(a) for a in x]
    station.append(x)
def check(arri):
    flag_check = True
    l = len(arri)
    r = 0
    for i in range(l):
        r += arri[i][0] - arri[i][1]
        if r < 0:
            flag_check = False
    return flag_check


for i in range(num):
    if check(station):
        print(i)
        break
    else:
        prom = station.pop(0)
        station.append(prom)
