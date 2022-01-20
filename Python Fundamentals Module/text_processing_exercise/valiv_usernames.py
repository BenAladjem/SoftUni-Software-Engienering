text = input().split(", ")
def is_valid(a):
    result = True
    if not 2 < len(a) < 17:
        result = False
    for i in a:
        if i < "-" or ("0" > i > "-") or( "A" > i > "9") or("a" < i < "_") or( "_" > i > "Z") or i > "z":
            result = False
    return result
for j in text:
    if is_valid(j):
        print(j)
