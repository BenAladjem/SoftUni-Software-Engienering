num = int(input())

even = set()
odd = set()
for row in range(1, num + 1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        even.add(name_sum)
    else:
        odd.add(name_sum)

sum_even = sum(even)
sum_odd = sum(odd)
#print(sum_odd)
#print(sum_even)

result = set()

if sum_odd == sum_even:
    result = odd.union(even)
elif sum_even > sum_odd:
    result = odd.symmetric_difference(even)
else:
    result = odd.difference(even)
print(', '.join([str(x) for x in result]))





