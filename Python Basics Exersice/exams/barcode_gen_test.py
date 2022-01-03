m = int(input())
n = int(input())
for i in range(m,n+1):
    flag = True
    j = str(i)
    symbol = 0
    for sym in j:
        symbol = int(sym)
        if symbol%2==0:
            flag = False
    if flag:
        print(i,end=' ')