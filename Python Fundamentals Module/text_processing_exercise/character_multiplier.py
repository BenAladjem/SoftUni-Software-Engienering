words = input().split()
word_one = words[0]
word_two = words[1]

total_sum = 0
shorter_word_len = min(len(word_one),len(word_two))
longer_word_len = max(len(word_one),len(word_two))
longer = True
longer_word = ""
if len(word_one) > len(word_two):
    longer_word = word_one
    longer = False
elif len(word_one) < len(word_two):
    longer_word = word_two
    longer = False
for i in range(shorter_word_len):
    word_one_curr_ch = ord(word_one[i])
    word_two_curr_ch = ord(word_two[i])
    total_sum+=word_two_curr_ch*word_one_curr_ch
if not longer:
    for j in range(shorter_word_len,longer_word_len):
        total_sum += ord(longer_word[j])
print(total_sum)


