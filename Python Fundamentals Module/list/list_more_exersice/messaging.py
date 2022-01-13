numbers = input().split()
text = input()
text_l = []
for c in text:
    text_l.append(c)

#print(text_l)
#print(numbers)
def sum_num(a):
    sum = 0
    for i in a:
        sum+= int(i)
    return sum

def take_sym(a,t):
    lon = len(t)
    if a > lon:
        a = a % lon
    p = t[a]
    t.pop(a)
    return p



l = []
for x in numbers:
    l.append(sum_num(x))
#print(l)
for j in l:
    print(take_sym(j,text_l),end='')