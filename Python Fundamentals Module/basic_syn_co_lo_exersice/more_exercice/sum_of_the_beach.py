text = input()
te = text.lower()
count = 0
l = len(te)

for i in range(0,int(l/2)):
    pos = 0
    if 'sand' in te:
        count+=1
        pos = te.index('sand')
        te = te[:pos] + te[pos+4:]
    elif 'water' in te:
        count+=1
        pos = te.index('water')
        te = te[:pos]+te[pos+5:]
    elif 'fish' in te:
        count+=1
        pos = te.index('fish')
        te = te[:pos]+te[pos+4:]
    elif 'sun' in te:
        count+=1
        pos = te.index('sun')
        te = te[:pos]+te[pos+3:]
print(count)
