m = int(input())
n = int(input())
count = 0
for i in range(m,n+1):
    sum_even = 0
    sum_odd = 0
    num_str = str(i)
    for j in num_str:
        count += 1
        if count%2==0:
            sum_even+=int(j)
        else:
            sum_odd+=int(j)
    if sum_odd==sum_even:
        print(i,end=' ')

