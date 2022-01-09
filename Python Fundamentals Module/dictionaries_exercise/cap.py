countries = input().split(", ")
capitals = input().split(", ")
d = dict(zip(countries,capitals))
for countries,capitals in d.items():
    print(f"{countries} -> {capitals}")
