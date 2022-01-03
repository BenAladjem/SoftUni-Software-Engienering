days = int(input())
days_win = 0
total_sum = 0
for i in range(1,days+1):
    command = ''
    count_win = 0
    count_lose = 0
    day_sum = 0
    while command!='Finish':
        sport = input()
        if sport == "Finish":
            break
        result = input()

        if result =='win':
            count_win+=1
            day_sum+=20
        else:
            count_lose+=1
        command = sport
    if count_win>count_lose:
        day_sum*=1.1
        days_win+=1

    total_sum+=day_sum
if days_win>days/2:
    total_sum*=1.2
    print(f"You won the tournament! Total raised money: {total_sum:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_sum:.2f}")


