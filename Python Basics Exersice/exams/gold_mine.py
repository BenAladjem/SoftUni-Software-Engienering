num_locations = int(input())
for i in range(0,num_locations):
    exp_yield = 0
    days = 0
    exp_yield = float(input())
    days = int(input())
    average_yield = 0
    for j in range(0,days):
        real_yeld_per_day = float(input())
        average_yield +=real_yeld_per_day
    average_yield = average_yield/days
    if exp_yield<=average_yield:
        print("Good job! Average gold per day: %.2f."%(average_yield))
    else:
        print("You need %.2f gold."%(exp_yield-average_yield))
