days = int(input())
hours = int(input())
day_count = 0
total = 0
for i in range(1,days+1):
    day_count+=1
    day_sum = 0
    for j in range(1,hours+1):
        if i%2==0 and not j%2==0:
            day_sum +=2.50
        elif not i%2==0 and j%2==0:
            day_sum+=1.25
        else:
            day_sum+=1
    print("Day: %d - %.2f leva"%(day_count,day_sum))
    total+=day_sum
print("Total: %.2f leva"%(total))
