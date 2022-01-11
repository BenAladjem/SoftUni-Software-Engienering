n = int(input())

l = [1,1,2]

for i in range(3,n):
    l.append(l[i-1]+l[i-2]+l[i-3])
for j in range(n):

    print(f"{l[j]} ",end='')