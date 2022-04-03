n = int(input())

elements = set()

for _ in range(n):
    #curent_el = input().split()
    [elements.add(x) for x in input().split()]

for el in elements:
    print(el)