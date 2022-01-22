import  re

text = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
valid_nums = re.finditer(pattern, text)
valid_nums = [num.group() for num in valid_nums]
print(' '.join(valid_nums))