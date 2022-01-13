rows = int(input())
cols = int(input())
m = []
for l in range(1,rows*cols+1):

    m.append(l)
count = 0
for i in range(rows):
    for j in range(cols):
        if m[count] >= 10:
            print(f" {m[count]}",end=' ')
        else:
            print(f"  {m[count]}",end=' ')
        count += 1
    print()