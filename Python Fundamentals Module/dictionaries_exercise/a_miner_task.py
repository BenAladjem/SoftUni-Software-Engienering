text = input()
collect = []
keys = []
values = []
while not text == "stop":
    collect.append(text)
    text = input()

for i in range(len(collect)):
    if i%2==0 and collect[i] in keys:
        x = int(values[collect.index(collect[i])])
        x += int(collect[i+1])
        values[collect.index(collect[i])] = str(x)
    elif i%2==0 and not collect[i] in keys:
        keys.append(collect[i])
    else:
        values.append(collect[i])
d = dict(zip(keys, values))
for (keys,values) in d.items():

    print(f"{keys} -> {values}")
