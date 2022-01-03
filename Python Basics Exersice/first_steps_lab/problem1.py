import math

budget = float(input())
students = int(input())
flour = float(input())
egg = float(input())
apron = float(input())

free_pack = students//5


needed_items = (math.ceil(students*1.2))*apron + students*egg*10 +(students - free_pack)*flour
if budget >= needed_items:
    print(f"Items purchased for {(needed_items):.2f}$.")
else:
    print(f"{(needed_items-budget):.2f}$ more needed.")