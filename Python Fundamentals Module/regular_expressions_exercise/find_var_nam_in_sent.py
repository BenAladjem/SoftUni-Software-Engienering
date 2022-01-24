import re
text = input()

#pattern = r'\b_\w+\b'
pattern = r'\b\_(?P<variable_name>[A-Za-z0-9]+)\b'
res = re.findall(pattern, text)
res = [x for x in res if not x =="_"]
print(",".join(res))
