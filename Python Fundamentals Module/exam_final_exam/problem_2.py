import re
num = int(input())
text = []
word = ""
pattern = r'^(?P<gr1>[\W|A-Z|a-z]{1,})[\>]([0-9]+)[|]([a-z]+)[|]([A-Z]+)[|]([^\<|\>]+)[\<](?P=gr1)$'
for i in range(num):

    t = input()
    #text.append(input())
    word = re.findall(pattern,t)

    if len(word) < 1:
        print("Try another password!")
    else:

        word = word.pop(0)
        w = word[0]

        word = "".join(word)
        word = word.replace(w,"")
        print(f"Password: {word}")

