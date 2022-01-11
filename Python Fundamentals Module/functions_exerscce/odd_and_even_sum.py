num = input()
def odd_sum(a):
    o_s = 0
    for i in a:
        if int(i)%2!=0:
            o_s+=int(i)
    return o_s
def even_sum(a):
    o_s = 0
    for i in a:
        if int(i)%2==0:
            o_s+=int(i)
    return o_s
print(f"Odd sum = {odd_sum(num)}, Even sum = {even_sum(num)}")