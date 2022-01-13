number_klients = int(input())
total_sum = 0
for i in range(1,number_klients+1):
    type_product = input()
    sum_klient = 0
    num_items = 0
    while type_product !='Finish':
        if type_product == 'basket':
            sum_klient+=1.5
        elif type_product == 'wreath':
            sum_klient+=3.8
        elif type_product == 'chocolate bunny':
            sum_klient+=7
        num_items+=1
        type_product = input()
    if num_items%2==0:
        sum_klient *=0.8
    total_sum+=sum_klient
    print(f"You purchased {num_items} items for {sum_klient:.2f} leva.")
awr_sum = total_sum/number_klients
print(f"Average bill per client is: {awr_sum:.2f} leva.")

