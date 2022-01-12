text = input().split(", ")
text = [int(a) for a in text]
max_gr = max(text)
for i in range(10, max_gr + 10, 10):
    l = [a for a in text if (i-10) < a <= i]
    print(f"Group of {i}'s: {l}")

    
