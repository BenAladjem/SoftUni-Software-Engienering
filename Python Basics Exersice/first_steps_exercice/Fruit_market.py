price_berries = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberries = float(input())
kg_berries = float(input())

price_raspberries = price_berries/2
price_oranges = price_raspberries*0.6
price_bananas = price_raspberries*0.2

sum_bananas = price_bananas*kg_bananas
sum_raspberries = price_raspberries*kg_raspberries
sum_oranges = price_oranges*kg_oranges
sum_berries = price_berries*kg_berries

total_sum = sum_berries+sum_oranges+sum_bananas+sum_raspberries
print(total_sum)