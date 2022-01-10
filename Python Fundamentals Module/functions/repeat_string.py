text = input()
num = int(input())
def repeat (a,b):
    new_text = ''
    for i in range(0,a):
        new_text+=b
    return new_text
print(repeat(num,text))