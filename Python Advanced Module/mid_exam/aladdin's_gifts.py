materials = [int(x) for x in input().split(' ')]
magic_levels = [int(x) for x in input().split(' ')]
magic_levels = magic_levels[::-1]
#print(magic_levels)
count_gemst = 0
count_porc = 0
count_gold = 0
count_diam = 0

while materials and magic_levels:
    magic = materials[-1] + magic_levels[-1]
    if magic < 100:
        if magic % 2 == 0:
            magic = materials[-1]*2 + magic_levels[-1] * 3
        else:
            magic = materials[-1]*2 + magic_levels[-1] * 2

        if 100 <= magic < 500:

            if 100 <= magic <= 199:
                count_gemst += 1
            elif 200 <= magic <= 299:
                count_porc += 1
            elif 300 <= magic <= 399:
                count_gold += 1
            elif 400 <= magic <= 499:
                count_diam += 1
            materials.pop()
            magic_levels.pop()
        else:
            materials.pop()
            magic_levels.pop()


    elif magic >= 500:
        magic /= 2
        if 100 <= magic < 500:
            if 100 <= magic <= 199:
                count_gemst += 1
            elif 200 <= magic <= 299:
                count_porc += 1
            elif 300 <= magic <= 399:
                count_gold += 1
            elif 400 <= magic <= 499:
                count_diam += 1
            materials.pop()
            magic_levels.pop()
        else:
            materials.pop()
            magic_levels.pop()
    else:
        if 100 <= magic <= 199:
            count_gemst += 1
        elif 200 <= magic <= 299:
            count_porc += 1
        elif 300 <= magic <= 399:
            count_gold += 1
        elif 400 <= magic <= 499:
            count_diam += 1
        materials.pop()
        magic_levels.pop()

if ((count_gemst > 0) and (count_porc > 0)) or ((count_gold > 0) and (count_diam > 0)):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_levels:
    magic_levels = magic_levels[::-1]
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
if count_diam > 0:
    print(f"Diamond Jewellery: {count_diam}")
if count_gemst > 0:
    print(f"Gemstone: {count_gemst}")
if count_gold > 0:
    print(f"Gold: {count_gold}")
if count_porc > 0:
    print(f"Porcelain Sculpture: {count_porc}")



