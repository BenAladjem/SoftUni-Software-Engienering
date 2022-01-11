a = int(input())
b = int(input())
c = int(input())

def sum_num(x,y):
    return x+y
def subtract(m,z):
    return  m-z
def add_and_sub(o,p,r):
    return  subtract(sum_num(o,p),r)
print(add_and_sub(a,b,c))