import sys
from io import StringIO

input1 = """2
Peter
Amy
Start
2
refill 1
1
End
"""
input2 = """10
Peter
George
Amy
Alice
Start
"""
sys.stdin = StringIO(input1)
#sys.stdin = StringIO(input2)

water_qantity = int(input())
