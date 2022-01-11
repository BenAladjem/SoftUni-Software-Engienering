text = input().split(' ')
nums = []
for el in text:
    nums.append(int(el))
command_data = input()
def exchange(nums_list,a):
    l1 = nums_list[:a+1]
    l2 = nums_list[a+1:]
    new_list = l2+l1
    return new_list

#def max():

#def min():



while command_data !="end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        index = int(command_data[1])
        print(exchange(text,index))
    elif command == "max":
        pass
    elif command == "min":
        pass
    elif command == "first":
        pass
    elif command == "last":
        pass

    command_data = input()





