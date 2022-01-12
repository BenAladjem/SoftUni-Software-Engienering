total_el = int(input())
electron_config = []
curent_l = 1

def el_per_level(l):
    result = 2*l**2
    return result

while total_el >0:
    if el_per_level(curent_l) <= total_el:
        electron_config.append(el_per_level(curent_l))
        total_el -= el_per_level(curent_l)
    else:
        electron_config.append(total_el)
        break

    curent_l +=1
print(electron_config)
