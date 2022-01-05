event = ''
count = 0
while event!="END":
    event = input()
    if event =='coding':
        count+=1
    elif event =='CODING':
        count+=2
    elif event == 'dog':
        count+=1
    elif event =='DOG':
        count+=2
    elif event == 'cat':
        count+=1
    elif event == 'CAT':
        count+=2
    elif event == 'movie':
        count += 1
    elif event == 'MOVIE':
        count += 2
    if count > 5:
        print("You need extra sleep")
        break
else:
    print(count)