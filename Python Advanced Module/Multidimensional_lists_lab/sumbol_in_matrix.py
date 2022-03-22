n = int(input())
matrix = []

for i in range(n):
    row = input()
    matrix.append(row)
symbol = input()

flag = True
for ro in range(n):

    text = matrix[ro]
    if symbol in text:
        print(f"({ro}, {text.index(symbol)})")
        flag = False
        break
if  flag:
    print(f"{symbol} does not occur in the matrix")