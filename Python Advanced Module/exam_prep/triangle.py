'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
'''
'''
1 a[0]+a[1]
'''
n = int(input())
row1 = [1]
row2 = [1,1]
row = [1, 1]

def next_row(n, row):
    new_row = [1]
    for i in range(0, n-1):
        new_row.append(row[i]+row[i+1])
    new_row.append(1)
    return new_row

print(row1)
print(row2)

for j in range(2, n):
    num_row = j
    row_j = next_row(j, row)
    print(row_j)
    row = row_j

#print(next_row(2,row2))
