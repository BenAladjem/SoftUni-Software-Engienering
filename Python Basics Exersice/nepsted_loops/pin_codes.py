import math

a = int(input())
b = int(input())
c = int(input())


def is_prime(x):
    flag = True
    for i in range(2,int(math.sqrt(x))+1):
        if  x%i==0:
            flag = False
        else:
            flag = True
    return flag

for i in range(1,a+1):
    for j in range(2,b+1):
        for k in range(1,c+1):
            if i%2==0 and k%2==0 and is_prime(j):
                print(i,j,k)