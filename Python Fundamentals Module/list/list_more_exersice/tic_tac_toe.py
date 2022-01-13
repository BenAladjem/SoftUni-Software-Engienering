f = input().split()
s = input().split()
t = input().split()
flag = False
for i in range(3):
    if f[i] == "1" and s[i] == "1" and t[i] == "1":
        print("First player won")
        flag = True
    elif f[i] == "2" and s[i] == "2" and t[i] == "2":
        print("Second player won")
        flag = True
if ((f[0] == "1" and f[1] == "1" and f[2] == "1")or(s[0] == "1" and s[1] == "1" and s[2] == "1")or(t[0] == "1" and t[1] == "1" and t[2] == "1")) :
    print("First player won")
    flag = True
elif ((f[0] == "2" and f[1] == "2" and f[2] == "2")or(s[0] == "2" and s[1] == "2" and s[2] == "2")or(t[0] == "2" and t[1] == "2" and t[2] == "2")) :
    print("Second player won")
    flag = True

elif f[0] == "1" and s[1] == "1" and t[2] == "1":
    print("First player won")
    flag = True
elif f[0] == "2" and s[1] == "2" and t[2] == "2":
    print("Second player won")
    flag = True
elif f[2] == "1" and s[1] == "1" and t[0] == "1":
    print("First player won")
    flag = True
elif f[2] == "2" and s[1] == "2" and t[0] == "2":
    print("Second player won")
    flag = True
if not flag:
    print("Draw!")