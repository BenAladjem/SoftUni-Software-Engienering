data = input()

cities = {}
while not data == "Sail":
    city,population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if not city in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold


    data = input()

data = input()

while not data =="End":
    data = data.split("=>")

#https://pastebin.com/br1SjttR
