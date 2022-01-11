text = input()
def password(a):
    l = len(a)
    flag = True
    if 6<=l<=10:
        None
    else:
        print("Password must be between 6 and 10 characters")
        flag = False
    f = False
    for i in a:

        if 48<=ord(i)<=57 or 97<=ord(i)<=122 or 65<=ord(i)<=90:
            None
        else:
            f = True
    if f :
        print("Password must consist only of letters and digits")
        flag = False
    count = 0
    for i in a:
        if 48<=ord(i)<=57:
            count+=1
    if count<2:
        print("Password must have at least 2 digits")
        flag = False
    if flag:
        print("Password is valid")
password(text)