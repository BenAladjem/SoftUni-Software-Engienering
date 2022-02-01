expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
p_indices = []

for index, ch in enumerate(expression):
    if ch == '(':
        p_indices.append(index)
    elif ch == ')':
        closing_index = index
        opening_index = p_indices.pop()
        print(expression[opening_index:closing_index + 1])
