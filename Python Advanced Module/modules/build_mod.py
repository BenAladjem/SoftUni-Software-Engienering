import random
import sys
from io import StringIO

test_in1 = '''1
2
3
4'''

sys.stdin = StringIO(test_in1)
print(sys.path)
#sys.stdout = StringIO('')

print(random.randint(1, 10))
print(sys.path.join('parent', 'child'))
