text = input()
text_list = text.split(" ")
new_list = []
for i in text_list:
    new_list.append(int(i) * (-1))
print(new_list)
