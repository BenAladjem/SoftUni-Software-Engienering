n = int(input())
for i in range(1111,10000):
    x=str(i)
    flag = True
    for j in x:
        j=int(j)
        if j==0:
            flag=False
            break
        if not n%j==0:
            flag = False
    if flag:
        print(x,end=' ')


