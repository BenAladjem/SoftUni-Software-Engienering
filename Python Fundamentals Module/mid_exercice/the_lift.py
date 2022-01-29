people_in = int(input())
people = people_in
lift = input().split(" ")
full_lift = []
num_wagons = len(lift)
seats = num_wagons * 4
free_seats = seats
for j in lift:
    free_seats -= int(j)
#print(free_seats)
for i in range(num_wagons):
    a = int(lift[i])
    seats -= a
    b = 4 - a

    if people >= 4:
        full_lift.append('4')
    elif people >= 0:
        full_lift.append(str(people+a))
    else:
        full_lift.append('0')
    people -= b

if people_in == 0:
    if free_seats ==0:
        print(" ".join(lift))
    else:
        print("The lift has empty spots!")
        print(" ".join(lift))

else:

    if people_in == free_seats:
        print(" ".join(full_lift))
    if people_in < free_seats:
        print("The lift has empty spots!")
        print(" ".join(full_lift))
    else:
        print(f"There isn't enough space! {people_in - free_seats} people in a queue!")
        print(" ".join(full_lift))

