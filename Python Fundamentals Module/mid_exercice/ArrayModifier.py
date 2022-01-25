arr = input().split(" ")
a = [int(x) for x in arr]
#print(arr)

c = input()
while not c == "end":

    com = c.split(" ")
    if com[0] == "swap":
        x = a[int(com[1])]
        a[int(com[1])]=a[int(com[2])]
        a.pop(int(com[2]))
        a.insert(int(com[2]),x)
    elif com[0] =="multiply":
        x = int(com[1])
        y = int(com[2])
        z = a[x]*a[y]
        a.pop(x)
        a.insert(x,z)
    elif com[0] == "decrease":
        a = [(m-1) for m in a]
    else:
        break

    #print(" ".join(str(a)))
    c = input()
a = [str(x) for x in a]
print(", ".join(a))
