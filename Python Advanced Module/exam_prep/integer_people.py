men = [int(x) for x in input().split(' ')]
women = [int(x) for x in input().split(' ')]

new_women = []

while women:
    new_women.append(women.pop())

count = 0
while new_women and men:
    # if men[-1] <= 0:
    #     men.pop()
    # if new_women[-1] <= 0:
    #     new_women.pop()
    while men[-1] <=0:
        men.pop()
    while new_women[-1] <= 0:
        new_women.pop()

    if men and new_women:
        if men[-1] % 25 == 0:
            men.pop()
            if men:
                men.pop()
        if new_women[-1] % 25 == 0:
            new_women.pop()
            if new_women:
                new_women.pop()
    if men and new_women:
        if men[-1] == new_women[-1]:
            count += 1
            men.pop()
            new_women.pop()
        else:
            new_women.pop()
            men[-1] = men[-1] - 2

men = [str(x) for x in men]
new_women = [str(x) for x in new_women]
print(f"Matches: {count}")
if men:
    print(f"Males left: {', '.join(men[::-1])}")
else:
    print("Males left: none")
if new_women:
    print(f"Females left: {', '.join(new_women[::-1])}")
else:
    print("Females left: none")


