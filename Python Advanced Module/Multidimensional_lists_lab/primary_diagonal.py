n = int(input())
matrix = []

for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

sum = 0
for j in  range(n):
    sum += matrix[j][j]

print(sum)