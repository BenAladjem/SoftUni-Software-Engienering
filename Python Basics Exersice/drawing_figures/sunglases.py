import math

n = int(input())
row_frame = math.ceil(n/2)-1
def first(a):
    print("*"*2*n+" "*n+"*"*2*n)
def between(a):
    print("*"+"/"*(2*n-2)+\
          "*"+" "*n+"*"+"/"*(2*n-2)+"*")
def frame(a):
    print("*" + "/" * (2 * n - 2) + \
          "*" + "|" * n + "*" + "/" * (2 * n - 2) + "*")
for i in range(0,n):
    if i==0 or i==n-1:
        first(n)
    elif i== row_frame:
        frame(n)
    else:
        between(n)
