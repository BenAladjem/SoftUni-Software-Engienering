some_text = "a b c d e f g h "
print(some_text)
result = some_text.split()
print(result)
back_to_string = "&*i".join(result)
print(back_to_string)
l = len(result)
hl = int(l/2)
text1 = result[0:hl]
text2 = result[hl:l]
print(text1)
print(text2)
j=1
for i in range(0,hl):
    text1.insert(j,text2[i])
    j+=2
print(text1)