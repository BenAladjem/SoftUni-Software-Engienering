from collections import deque

first_row = deque([int(x) for x in input().split(', ') if int(x)>0])
second_row = [int(x) for x in input().split(', ') if int(x)>0]
#sr = deque
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworcs = 0

flag = False

#print(first_row)
#print(second_row)

# for el in first_row:
#     if el < 0:
#         first_row.remove(el)
#     #print(first_row)
# for e in second_row:
#     if e <= 0:
#         second_row.remove(e)



while (len(first_row)>0 and len(second_row)>0):
    '''or (palm_fireworks <3
                    and willow_fireworks <3
                    and crossette_fireworcs <3):'''
    l = len(first_row)
    for i in range(l):
    #while not flag:
        sum = first_row[0] + second_row[-1]
        if sum%3 == 0 and sum % 5 ==0:
            crossette_fireworcs += 1
            first_row.popleft()
            second_row.pop()
            l = len(first_row)
        elif sum % 3 ==0:
            palm_fireworks +=1
            first_row.popleft()
            second_row.pop()
            l = len(first_row)
        elif sum % 5 == 0:
            willow_fireworks += 1
            first_row.popleft()
            second_row.pop()
            l = len(first_row)
        else:
            a = first_row[0]-1
            first_row.popleft()
            first_row.append(a)

            #second_row.append(sum)

        if palm_fireworks>2 and willow_fireworks>2 and crossette_fireworcs>2:
            flag = True
            break
    if flag:
        break
    #print(first_row)
    #print(second_row)
if flag:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")
if first_row:
    print(f"Firework Effects left: {', '.join(str(x) for x in first_row)}")
if second_row:
    print(f"Explosive Power left: {', '.join([str(x) for x in second_row])}")

print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworcs}')

