text = input()
text = [x for x in text if not x ==" "]
keys = []
values = []
for i in range (len(text)):
    if  text[i] not in keys:
        keys.append(text[i])
for l in keys:
    values.append(text.count(l))

# for j in keys:
#      print(f"{j} -> {text.count(j)}")

#print(keys)
#print(values)
d = dict(zip(keys,values))
for (keys, values) in d.items():
    print(f"{keys} -> {values}")








