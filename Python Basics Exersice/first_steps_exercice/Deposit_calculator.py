dep_sum=float(input())
time = int(input())
interest = float(input())

all_inter = dep_sum*interest/100
int_per_mont = all_inter/12
total_sum = dep_sum+(time*int_per_mont)
print(total_sum)