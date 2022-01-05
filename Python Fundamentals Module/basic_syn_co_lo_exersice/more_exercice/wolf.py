text = input()
l = text.split(", ")
pos = len(l)-l.index("wolf")-1
if l[-1]=="wolf":
    print('Please go away and stop eating my sheep')
else:
    print(f"Oi! Sheep number {pos}! You are about to be eaten by a wolf!")

