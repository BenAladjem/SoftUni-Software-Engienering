raw_activation_key = input()

data = input()
while not data =="Generate":
    data = data.split(">>>")
    if data[0] == "Contains":
        substring = data[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif data[0] =="Flip":
        state = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
    elif data[0] == "Upper":
        pass
    elif data[0] == "Slice":

        start_index = int(data[1])
        end_index = int(data[2])
        first_part = raw_activation_key[:start_index]
        last_part = raw_activation_key[end_index:]
        raw_activation_key = first_part + last_part


    data = input()
#https://pastebin.com/1GttXAXC
