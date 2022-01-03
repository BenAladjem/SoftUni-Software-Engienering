num_custom = int(input())
total_sum = 0
for i in range(1,num_custom+1):
    sum_custom = 0
    count_even = 0
    product = input()
    while not product=="Finish":
        count_even+=1
        if product == 'basket':
            sum_custom+=1.5
        elif product == 'wreath':
            sum_custom += 3.8
        else:
            sum_custom +=7
        product = input()
    if count_even%2==0:
        sum_custom*=0.8
    print("You purchased %s items for %.2f leva."%(count_even,sum_custom))
    total_sum+=sum_custom
print("Average bill per client is: %.2f leva."%(total_sum/num_custom))