import math

command = input()
sum_prime = 0
sum_non_prime = 0
while not command =="stop":
    num = int(command)
    if num<0:
        print('Number is negative.')
    else:
        kur_num = int(math.sqrt(num))
        flag = False
        for i in range(2,kur_num+1):
            if num%i==0:
                flag = True
        if flag:
            sum_non_prime+=num
        else:
            sum_prime+=num
    command=input()
print("Sum of all prime numbers is:",sum_prime)
print("Sum of all non prime numbers is:",sum_non_prime)