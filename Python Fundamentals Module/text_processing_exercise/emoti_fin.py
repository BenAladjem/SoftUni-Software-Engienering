import re
text = input()

pattern = r'\:((\w*)|[!-+]*)'
matches = re.finditer(pattern, text)
for i in matches:
    print(i)