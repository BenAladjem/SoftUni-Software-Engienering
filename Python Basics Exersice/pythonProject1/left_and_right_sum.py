import math

n= int(input())
sum_l = 0
sum_r = 0
for i in range (0,n*2):
    num = int(input())
    if i<n:
        sum_l+=num
    else:
        sum_r+=num
#print(sum_l)
#print(sum_r)
if sum_l==sum_r:
    print('Yes, sum =',sum_l)
else:
    print('No, diff =',int(math.fabs(sum_l-sum_r)))