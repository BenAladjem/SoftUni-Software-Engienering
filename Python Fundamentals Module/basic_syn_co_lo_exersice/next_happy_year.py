year = int(input())
list = []
flag = ''
while (flag !=False):
    flag = False
    list = []
    year+=1
    year=str(year)
    for i in year:
        list.append(i)
    l = len(list)
    for j in range(0,l):
        if list[j] in list[j+1:l]:
            flag = True
            break
    if flag ==False:
        print(year)
        break
    else:
        year=int(year)
        flag = True