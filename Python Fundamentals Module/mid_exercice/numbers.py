numbers = input().split(" ")
numbers = [int(x) for x in numbers]
count_numbers = len(numbers)
sum_num = 0
for i in range(count_numbers):
    sum_num +=int(numbers[i])
awr_num = sum_num / count_numbers
#print(awr_num)
bigest_num = [x for x in numbers if x > awr_num]
#print(bigest_num)
bigest_num.sort()
#print(bigest_num)
b = bigest_num[::-1]
b = [str(x) for x in b]
br = []
for y in range(5):
    if y < len(b):
        br.append(b[y])
if len(br) >0:
    print(" ".join(br))
else:
    print("No")