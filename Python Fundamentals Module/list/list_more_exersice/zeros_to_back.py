l = input().split(", ")
print(l)
number = l.count("0")
for i in range(number):
    l.remove("0")
    l.append("0")
result = []
for n in l:
    result.append(int(n))
print(result)





