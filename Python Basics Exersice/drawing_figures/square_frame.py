n = int(input())
def first(a):
    print("+","- "*(n-2),end='')
    print("+")

def between(a):
    print("|","- "*(n-2),end='')
    print("|")
for i in range(1,n+1):
    if i==1 or i==n:
        first(n)
    else:
        between(n)