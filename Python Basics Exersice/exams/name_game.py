n = ''
best_result = 0
winner = ''
while n!="Stop":
    points = 0
    l = len(n)
    name = n
    for i in range(0,l):
        num = int(input())
        if num==ord(name[i]):
            points+=10
        else:
            points+=2
    if points>=best_result:
        best_result=points
        winner = name
    n = input()
print("The winner is "+winner+" with "+str(best_result)+" points!")