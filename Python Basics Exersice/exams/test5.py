name = input()
l = len(name)
winner = ''
max_points = 0

points = 0
for i in range (0,l):
    num = int(input())
    if num == ord(name[i]):
        points+=10
    else:
        points+=2
