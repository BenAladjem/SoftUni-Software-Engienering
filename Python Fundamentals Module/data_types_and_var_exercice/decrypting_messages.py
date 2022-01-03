key = int(input())
number = int(input())
for i in range(number):
    print(chr(key+ord(input())),end='')
