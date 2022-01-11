l = []
for i in range(3):
    l.append(int(input()))
flag = True
count = 0
for j in l:
    if j < 0:
        count += 1
if 0 in l:
    print("zero")
    flag = False
if flag:
    if count==1 or count==3:
        print("negative")

    else:
        print("positive")


