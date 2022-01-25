collection = input().split(", ")
command = ''
while not command == "Craft!":

    command = input()
    if command == "Craft!":
        break
    else:
        text = command.split(" - ")
    if text[0]== "Collect":
        if not text[1] in collection:
            collection.append(text[1])

    elif text[0] == "Drop":
        if text[1] in collection:
            collection.remove(text[1])

    elif text[0] == "Combine Items":
        items = text[1].split(":")
        if items[0] in collection:
            a = collection.index(items[0])
            collection.insert(a+1,items[1])

    elif text[0] == "Renew":
        if text[1] in collection:
            collection.remove(text[1])
            collection.append(text[1])

print(", ".join(collection))


