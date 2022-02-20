clothes = [int(x) for x in input().split()]
#clotes = clotes[::-1]
rack_capacity = int(input())
used_racks = 1
curent_rack_capacity = rack_capacity
#print(clotes)
#a = clotes.pop()
#print(a)
#print(clotes)
while clothes:
    clot = clothes.pop()
    if curent_rack_capacity >= clot:
        curent_rack_capacity -= clot
    else:
        used_racks += 1
        curent_rack_capacity = rack_capacity
        curent_rack_capacity -= clot

print(used_racks)