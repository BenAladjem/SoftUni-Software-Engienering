from collections import deque
import sys

input1 = """George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End
"""

input2 = """Anna
Emma
Alexander
End
"""

#sys.stdinIO(input1)
#sys.stdinIO(input2)

queue = deque()
while True:
    command = input()
    if command == 'End':
        print(f'{len(queue)} people remaining')
        break
