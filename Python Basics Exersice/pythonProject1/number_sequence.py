n= int(input())
max_number=-999999999999
min_number=999999999999
for i in range (0,n):
    num = int(input())
    if min_number > num:
        min_number=num
    if max_number < num:
        max_number = num
print('Max number:',max_number)
print('Min number:',min_number)