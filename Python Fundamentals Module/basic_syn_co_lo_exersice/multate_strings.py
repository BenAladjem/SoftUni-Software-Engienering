text1 = input()
text2 = input()

new_text = ''
l = len(text1)
for i in range(l):
    if text1[i]!=text2[i]:
        new_text = text2[:i+1]+text1[i+1:]
        print(new_text)