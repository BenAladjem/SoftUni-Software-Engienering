quantity = int(input())
orders = input().split()
orders = [int(x) for x in orders]
orders_complete = [str(x) for x in orders]
bigest_order = max(orders)

flag = True
for i in range(len(orders)):
    if quantity >= orders[i]:
        quantity -= orders[i]
        orders_complete.remove(str(orders[i]))
    else:
        print(bigest_order)
        #orders = [str(x) for x in orders]
        print(f'Orders left: {" ".join(orders_complete)}')
        flag = False
        break
if flag:
    print(bigest_order)
    print("Orders complete")
