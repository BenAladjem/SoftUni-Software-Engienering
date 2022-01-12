worlds = input().split()

text = [a for a in worlds if len(a)%2==0]
for i in text:
    print(i)