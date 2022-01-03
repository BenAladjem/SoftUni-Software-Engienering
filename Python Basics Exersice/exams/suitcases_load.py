tank_vol = float(input())
command = input()
count = 0
free_tank = tank_vol
while command!='End':
    case = float(command)
    count += 1
    if count%10==3:
        case*=1.1
    if free_tank<case:
        print('No more space!')
        count-=1
        break
    else:
        free_tank-=case

    command = input()
    if command =='End':
        print("Congratulations! All suitcases are loaded!")
        break
print(f"Statistic: {count} suitcases loaded.")