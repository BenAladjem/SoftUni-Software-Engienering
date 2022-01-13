numbers = input().split()
count = int(input())
l = len(numbers)
result = []
x = 0
while numbers:
    if count > l:
        n = count%l
        result.append(numbers[n-1])
        numbers.pop(n-1)
    else:
        for i in range(count-1-x,l,count):
            result.append(numbers[i])
        m = 0
        for j in range(count-1-x,l,count):
            numbers.pop(j - m)
            m+=1
        x = (l+x) % count
    l = len(numbers)
res = []

#print(result)

for g in result:
    res.append(int(g))

print("[",end='')
for a in range(len(res)):
    if a != len(res)-1:
        print(f"{res[a]},", end='')
    else:
        print(f"{res[a]}",end='')
print("]")
