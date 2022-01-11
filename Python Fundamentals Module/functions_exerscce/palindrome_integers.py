text = input()
list = text.split(', ')

def is_palindrome(a):
    l_p =[]
    for i in a:
        l_p.append(i)
    l = len(l_p)
    flag = True
    for j in range(0,int(l/2)):
        if l_p[j]!=l_p[l-j-1]:
            flag = False
            break
    return flag

for i in list:
    print(is_palindrome(i))



