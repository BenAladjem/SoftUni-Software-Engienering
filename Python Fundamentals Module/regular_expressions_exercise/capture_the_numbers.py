import re

command = input()
text = ''
result = []
while command:
    text+=command
    # pattern = r'\d+'
    # m = re.finditer(pattern, command)
    # m = [n.group() for n in m]
    # result.append(m)
    command = input()

pattern = r'\d+'
m = re.findall(pattern, text)
print(*m)