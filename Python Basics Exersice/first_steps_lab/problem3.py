products = [x for x in input().split("|")]
#print(products)
command = input()
while not command == "Shop!":
    action = command.split("%")
    com = action[0]
    if com == "Important":
        prod = action[1]
        if prod in products:
            products.remove(prod)
            products.insert(0,prod)
        else:
            products.insert(0,prod)
    elif com == "Add":
        prod = action[1]

        if not prod in products:
            products.append(prod)
        else:
            print("The product is already in the list.")
    elif com =="Swap":
        prod = action[1]

        prod2 = action[2]
        if (prod2 in products) and (prod in products):
            i1 = products.index(prod)
            i2 = products.index(prod2)
            products.pop(i1)
            products.insert(i1,prod2)
            products.pop(i2)
            products.insert(i2,prod)
        else:
            if prod in products:
                print(f"Product {prod2} missing!")
            else:
                print(f"Product {prod} missing!")

    elif com == "Remove":
        prod = action[1]

        if prod in products:
            products.remove(prod)
        else:
            print(f"Product {prod} isn't in the list.")
    elif com  =="Reversed":
        products.reverse()

    command = input()
l = len(products)
for i in range(1,l+1):
    print(f"{i}. {products[i-1]}")

