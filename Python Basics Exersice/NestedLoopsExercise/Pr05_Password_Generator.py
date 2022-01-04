n = int(input())
l = int(input())
for i in range(1,n):
    for j in range(1,n):
        for k in range(97,97+l):
            for m in range(97,97+l):
                if i>j:
                    x=i
                else:
                    x=j
                for c in range(x+1,n+1):
                    print("%d%d%s%s%d"%(i,j,chr(k),chr(m),c),end=' ')
