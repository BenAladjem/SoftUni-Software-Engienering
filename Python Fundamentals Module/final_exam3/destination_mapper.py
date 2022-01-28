import re

text = input()
w = []
ww = []

travel_points = 0
pattern = r'(?P<gr1>[\=]|[\/])([A-Z][A-Za-z]{3,})(\1)'
words = re.finditer(pattern,text)
for word in words:
    w.append(word.group())
for x in w:
    ww.append(x[1:-1])
    travel_points += len(x[1:-1])

print("Destinations:",end=' ')
print(", ".join(ww))
print(f"Travel Points: {travel_points}")