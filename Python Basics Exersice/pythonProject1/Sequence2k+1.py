n = int(input())
result = 1
for num in range(1,n+1):
    print(result)
    result = result*2+1
    if result >n:
        break