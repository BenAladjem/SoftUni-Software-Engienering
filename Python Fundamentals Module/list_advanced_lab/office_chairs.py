rooms = int(input())
chairs = []
flag = True
for i in range (rooms):
    chairs.append(input().split(' '))
#print(chairs)
sum_chairs = 0
for j in range(len(chairs)):
    if len(chairs[j][0])< int(chairs[j][1]):
        print(f"{(int(chairs[j][1])-(len(chairs[j][0])))} more chairs needed in room {j+1}")
        flag = False
    else:
        sum_chairs += (len(chairs[j][0])) - (int(chairs[j][1]))
if flag:
    print(f"Game On, {sum_chairs} free chairs left")