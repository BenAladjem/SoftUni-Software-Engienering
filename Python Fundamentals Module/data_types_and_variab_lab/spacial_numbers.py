n = int(input())

for num in range(1,n+1):
    flag: bool = False
    sum = 0
    i=num
    while i>0:
        sum += i%10
        i = i//10
    if sum==5 or sum ==7 or sum ==11:
        flag = True
    print(f"{num} -> {flag}")