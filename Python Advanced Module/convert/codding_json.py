import json

with open('persons.json') as h:
    data = json.load(h)
print(data)
code_data = str(data).encode()
print(code_data)
newstring = bytes(str(data), 'utf-16')
print(newstring)