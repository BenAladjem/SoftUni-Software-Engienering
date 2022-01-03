voucher = int(input())
bought_tick_count = 0
other_purchase_count = 0

total_total = voucher
command = input()
while command != 'End':
    purchase = command

    if len(purchase) > 8:
        bought_tick_count += 1
        price1 = ord(purchase[0])
        price2 = ord(purchase[1])
        result = price1 + price2
        total_total -= result
        if total_total < 0:
            bought_tick_count -= 1
            break
    else:
        other_purchase_count += 1
        price = ord(purchase[0])
        total_total -= price
        if total_total < 0:
            other_purchase_count -= 1
            break
    #if total_total < 0:
       # break
    command = input()
print(bought_tick_count)
print(other_purchase_count,end='')