days = int(input())
cooks = int(input())
cake = int(input())
gofr = int(input())
pancakes = int(input())

price_cake= cake*45
price_gofr = gofr*5.80
price_pancakes = pancakes*3.2

sum_per_day = (price_pancakes+price_gofr+price_cake)*cooks
all_sum = sum_per_day*days
total_sum = all_sum*7/8
print(total_sum)
