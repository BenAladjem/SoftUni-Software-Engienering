import sys

max_num = -sys.maxsize
nums = input()
while nums!="Stop":
    n = int(nums)
    if max_num<n:
        max_num = n
    nums = input()
else:
    print(max_num)

