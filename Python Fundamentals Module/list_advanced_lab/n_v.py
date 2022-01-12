text = input().split(".")
a = ''
for b in text:
    a += b
c = str(int(a) +1)
result = ".".join(c)
print(result)