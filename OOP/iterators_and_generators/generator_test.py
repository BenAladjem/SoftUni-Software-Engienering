word = 'asdfghj4klpoiuytrewq'
def first_n(n):
    num = 2
    while num <= n:
        yield word[num]
        num += 1

def for_test(t):
    for x in range(2, len(t)-5):
        yield t[x]

l = []
s = ''
sx = ''
for el in first_n(6):
    #print(el)
    l.append(el)
    s += el
    print(l)
    print(s)

for el in for_test(word):
    sx += el
    print(sx)