countries = input().split(", ")
capitals = input().split(", ")

country_capital = dict(zip(countries,capitals))

for (countries, capitals) in country_capital.items():
    print(f"{countries} -> {capitals}")