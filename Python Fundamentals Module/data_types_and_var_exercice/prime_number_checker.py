num = int(input())
def prime(a):
    flag = True
    for i in range(2,int(a/2)+1):
        if a % i == 0:
            flag = False
    return flag
print(prime(num))
