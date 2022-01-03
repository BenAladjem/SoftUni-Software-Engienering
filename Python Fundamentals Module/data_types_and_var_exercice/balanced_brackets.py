num = int(input())
check_sum = 0
flag = True
for i in range(num):
    symol = input()
    if symol == "(":
        check_sum +=1
    elif symol ==")":
        check_sum -= 1
    if check_sum < 0 or check_sum >1:
        flag = False
if check_sum == 0 and flag:
    print("BALANCED")
else:
    print("UNBALANCED")