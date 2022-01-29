first_count = int(input())
second_count = int(input())
third_count = int(input())

people_count = int(input())
people_per_count = first_count + second_count + third_count

hours = 0

while people_count > 0:
    hours += 1
    people_count -= people_per_count

    if hours% 4 ==0:
        hours+=1
print(f"Time needed: {hours}h.")