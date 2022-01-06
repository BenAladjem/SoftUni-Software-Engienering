import math

n=int(input())
sum_even =0
sum_odd = 0
for i in range (1,n+1):
    num = int(input())
    if i%2==0:
        sum_even+=num
    else:
        sum_odd+=num
#print(sum_even)
#print(sum_odd)
diff=int(math.fabs(sum_odd-sum_even))
if diff==0:
    print('Yes')
    print('Sum =',sum_odd)
else:
    print('No')
    print('Diff =',diff)