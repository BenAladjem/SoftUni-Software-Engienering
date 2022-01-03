m = input()
n = input()
lm = []
ln = []

for i in m:
    lm.append(int(i))
for i in n:
    ln.append(int(i))

for i in range(lm[0],ln[0]+1):
    for j in range(lm[1],ln[1]+1):
        for k in range(lm[2],ln[2]+1):
            for l in range(lm[3],ln[3]+1):
                if not i % 2 == 0 and not j % 2 == 0 and not k % 2 == 0 and not l % 2 == 0:
                    print(f'{i}{j}{k}{l} ', end='')