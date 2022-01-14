text = input()
num = int(input())
list_str = text.split(" ")
list_int = []
for i in list_str:
    list_int.append(int(i))
for j in range(num):
    x = min(list_int)
    list_int.remove(x)
for k in range(len(list_int)):
    if k == len(list_int)-1:
        print(f"{list_int[k]}")
    else:
        print(f"{list_int[k]}, ",end='')