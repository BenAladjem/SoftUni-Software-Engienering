from collections import deque
qq_slow = []
ss = []

qq = deque()
n = 100000

for i in range (n):
    qq_slow.append(i)

end = time()
print(f'Slow enque Exequted in {end - start}')
start = time