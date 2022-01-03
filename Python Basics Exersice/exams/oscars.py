name_act = input()
points_academy = float(input())
num_joury = int(input())
total_point = points_academy
for i in range(0, num_joury):
    points = 0
    name_joury = input()
    points = float(input())
    points = len(name_joury) * points / 2
    total_point += points
    if total_point > 1250.5:
        break
if total_point < 1250.5:
    print("Sorry, %s you need %.1f more!" % (name_act, 1250.5 - total_point))
else:
    print(f"Congratulations, {name_act} got a nominee for leading role with %.1f!" % (total_point))
