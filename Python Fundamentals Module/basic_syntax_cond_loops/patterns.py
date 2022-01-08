n = int(input())
def top(a):
    for i in  range(1,a+1):
        print("*"*i)
def floor(a):
    for i in range(a-1,0,-1):
        print("*"*i)

top(n)
floor(n)