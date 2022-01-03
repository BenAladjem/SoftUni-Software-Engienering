from math import floor

word = input()
mpw = ''
max_sum = 0
while word!='End of words':
    c = word[0]
    sum_ascii = 0
    for i in word:
        sum_ascii+=ord(i)
    if c =='a' or c=='e'or c=='i'\
        or c=='o'or c=='u'or c=='y'or\
        c=='A'or c=='E'or c=='I'or c=='O' \
        or c=='U'or c=='Y':
        sum_ascii*=len(word)
    else:
        sum_ascii = floor(sum_ascii/len(word))
    if sum_ascii > max_sum:
        max_sum=sum_ascii
        mpw = word
    word = input()
print('The most powerful word is '+mpw+' - '+str(max_sum))


