type_year = input()
holidays = int(input())
weekends_home = int(input())
all_weekend = 48
weekends_in_sofia = all_weekend-weekends_home
games_in_sofia = weekends_in_sofia*3/4
games_in_home = weekends_home
holidays_game = holidays*2/3
total_games = games_in_home+games_in_sofia+holidays_game
if type_year =="leap":
    total_games*=1.15
print(int(total_games))
