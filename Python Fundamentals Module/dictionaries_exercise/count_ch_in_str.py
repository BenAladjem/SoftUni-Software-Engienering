text = input()
text = [a for a in text if not a == " "]
#print(text)
keys = []
values = []
for i in text:
    if not i in keys:
        keys.append(i)
        values.append(text.count(i))
        #print(f"{keys} -> {values}")
        print(f"{i} -> {text.count(i)}")
d = dict(zip(keys,values))
print(d)
for keys,values in d.items():
    print(f"{keys} -> {values}")