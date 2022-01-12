#numbers = input().split(", ")
num_int = list(map(int,input().split(', ')))
positive = []
#positive = [str(num) for num in num_int if num >=0]
negative = []
even = []
odd = []
#for i in numbers:
#    num_int.append(int(i))
#print(num_int)
for j in num_int:
    if j >=0:
        positive.append(str(j))
    else:
        negative.append(str(j))
    if j%2==0:
        even.append(str(j))
    else:
        odd.append(str(j))

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")

