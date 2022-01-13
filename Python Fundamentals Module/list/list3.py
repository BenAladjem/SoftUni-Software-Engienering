num = int(input())
big_list = []
for i in range(0, num):
    row = input()
    list1 = []
    for j in row:
        list1.append(int(j))
    big_list.append(list1)
print(big_list)
