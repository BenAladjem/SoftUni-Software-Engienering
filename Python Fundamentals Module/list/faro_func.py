cards = input()
num = int(input())
card_list = cards.split(" ")
def mish_mash (a):
    lend = len(a)
    half_lend = int(lend / 2)
    card1 = a[0:half_lend]
    card2 = a[half_lend:lend]
    new_card_list = card1
    j = 1
    for i in range(half_lend):
        new_card_list.insert(j, card2[i])
        j += 2
    return new_card_list
for i in range(num):
    card_list = mish_mash(card_list)
print(card_list)
