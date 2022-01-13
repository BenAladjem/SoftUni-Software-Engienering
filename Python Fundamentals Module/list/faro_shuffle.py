cards = input()
num = int(input())
card_list = cards.split(" ")
for k in range(num):
    lend = len(card_list)
    half_lend = int(lend / 2)
    card1 = card_list[0:half_lend]
    card2 = card_list[half_lend:lend]
    new_card_list = card1
    j = 1
    for i in range(half_lend):
        new_card_list.insert(j, card2[i])
        j += 2
    card_list = new_card_list
print(card_list)
