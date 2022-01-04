import sys

min_num = sys.maxsize
nums = input()
while nums!="Stop":
    n = int(nums)
    if min_num > n:
        min_num = n
    nums = input()
else:
    print(min_num)

