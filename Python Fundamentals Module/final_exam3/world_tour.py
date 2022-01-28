text = input()
command = input()
while not command == "Travel":
    action = command.split(":")
    if action[0] == "Add Stop":
        index = int(action[1])
        word = action[2]
        l = len(text)
        if 0 <= index < l:
            text = text[:index]+word+text[index:]
        print(text)
    elif action[0] == "Remove Stop":
        start_index = int(action[1])
        end_index = int(action[2])
        l = len(text)
        if (0 <= start_index<= end_index) and (end_index < l):
            text = text[:start_index]+text[end_index+1:]
        print(text)
    elif action[0] == "Switch":
        old_string = action[1]
        new_string = action[2]
        if old_string in text:

            text = text.replace(old_string,new_string,1)
        print(text)


    command = input()
print(f"Ready for world tour! Planned stops: {text}")