num = int(input())
l = []
count = 1
while num > 0:
    el = 2*(count**2)
    if el <= num:
        l.append(el)
    else:
        l.append(num)
    num -=el
    count+=1

print(l)