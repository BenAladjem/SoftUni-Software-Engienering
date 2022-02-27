
def shopping_list(*args, **kwargs):
    result = []
    products = []
    all = []
    for el in args:
        result.append(el)
        all.append(result)
    for elem in kwargs:
        products.append(elem)
        products.append(kwargs[elem])
    all.append(products)
    if int(all[0][0]) < 100:
        return "You do not have enough budget."
    else:
        for i in range(len(all[1])):
        #return all[1][2]
            name = all[1][i]





print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
#print(shopping_list(20,
                    #jeans=(19.99, 1),
                   #))
#print(shopping_list(104,
                    #cola=(1.20, 2),
                    #candies=(0.25, 15),
                    #bread=(1.80, 1),
                    #pie=(10.50, 5),
                    #tomatoes=(4.20, 1),
                    #milk=(2.50, 2),
                    #juice=(2, 3),
                    #eggs=(3, 1),
                    #))
