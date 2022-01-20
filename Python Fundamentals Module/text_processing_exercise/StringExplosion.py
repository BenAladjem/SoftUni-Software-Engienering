text =[x for x in input()]
print(text)
li = []
power = 0
for i in range(len(text)-1):
    power = 0
    if text[i] == '>':
        if text[i+1].isnumeric():
            p= int(text[i+1])
            power +=p
        #li.append(i+1)
            for j in range(i+1,i+1+power):
                if not text[j]=='>':

                    text.pop(j)
                else:
                    if not text[j+1].isnumeric():
                        p_next = int(text[j+1])
                        power += int(p_next)
print(text)