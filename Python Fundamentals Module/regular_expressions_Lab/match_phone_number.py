import re

pattern = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'
text = input()

matches = re.finditer(pattern, text)
#for match in matches:
    #print(match.group())
valid_phones = [match.group() for match in matches]
print(", ".join(valid_phones))