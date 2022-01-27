text = input()
command = input()
while not command == "End":
    action = command.split()
    if action[0] == "Translate":
        ch = action[1]
        rep = action[2]
        text = text.replace(ch,rep)
        print(text)
    elif action[0] == "Includes":
        stri = action[1]
        if stri in text:
            print("True")
        else:
            print("False")
    elif action[0] == "Start":
        start = action[1]
        ls = len(start)
        if text[:ls] == start:
            print("True")
        else:
            print("False")
    elif action[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif action[0] == "FindIndex":
        char_in = action[1]
        l = len(text)
        text_rev = text[::-1]
        ind = text_rev.index(char_in)
        print(l-ind - 1)
    elif action[0] == "Remove":
        start_index = int(action[1])
        count = int(action[2])
        text = text[:start_index]+text[start_index+count:]
        print(text)
    command = input()