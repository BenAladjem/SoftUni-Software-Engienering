num_days = int(input())
total_sum = 0
day_win = 0
day_lose = 0
for i in range(0,num_days):
    count_win = 0
    count_lose = 0
    sum_day = 0
    inp = input()
    while not inp =='Finish':
        type_sport = inp
        result = input()
        if result =="win":
            sum_day+=20
            count_win+=1
        else:
            count_lose +=1
        inp = input()
    if count_win>count_lose:
        day_win+=1
        sum_day=1.1 * sum_day
    else:
        day_lose +=1
    total_sum+=sum_day
if day_win>day_lose:
    total_sum*=1.2
    print("You won the tournament! Total raised money: %.2f"%(total_sum))
else:
    print("You lost the tournament! Total raised money: %.2f"%(total_sum))

