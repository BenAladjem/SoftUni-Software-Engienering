text = input()
text = [x for x in text]
emoji = []

for i in text:

    if i == ":" and (text.index(":")+1)< len(text) and not text[text.index(":")+1].isnumeric():
        print(text[text.index(":")]+text[text.index(":")+1])
        text.pop(text.index(":"))
#print(emoji)