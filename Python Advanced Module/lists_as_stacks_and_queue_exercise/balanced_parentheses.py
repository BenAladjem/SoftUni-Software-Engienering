parentheses = input()

my_stack = []
flag = True
if parentheses[0] in ')}]':
    flag = False
    #print("No")

else:
    my_stack.append(parentheses[0])
    for el in range(1,len(parentheses)):

        if my_stack[-1] == "(" and parentheses[el] == ")" or\
             my_stack[-1] == "{" and parentheses[el] == "}"or\
             my_stack[-1] == "[" and parentheses[el] == "]":
            my_stack.pop()
        else:
            my_stack.append(parentheses[el])
if my_stack:
    flag = False
if flag:
    print("YES")
else:
    print("NO")
