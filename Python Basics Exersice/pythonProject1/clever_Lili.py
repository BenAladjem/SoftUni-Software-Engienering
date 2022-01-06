age = int(input())
price_wash= float(input())
price_toy = int(input())

count_toys = 0
money =0
sum_money=0
total_sum=0.0
for i in range(1,age+1):
    if(i%2==0):
        money+=10
        sum_money+=money-1
    else:
        count_toys+=1
total_sum=sum_money+count_toys*price_toy
if price_wash<=total_sum:
    print("Yes! {:.2f}".format(total_sum-price_wash))
else:
    print("No! {:.2f}".format(price_wash-total_sum))
