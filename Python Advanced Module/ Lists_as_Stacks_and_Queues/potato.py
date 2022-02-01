from collections import deque

potatos = input().split(" ")
potatos_queue = deque(potatos)
step = int(input())

while potatos_queue:
    for _ in range(step - 1):
        potatos_queue.append(potatos_queue.pop())