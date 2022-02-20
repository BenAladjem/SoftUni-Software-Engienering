import sys
from io import StringIO

input1 = """1 2 3 4 5"""

input2 = """1"""

sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

text = input().split(' ')

result = []

while text:
    el = text.pop()
    result.append(el)
#text = text[::-1]
print(" ".join(result))

