text = input()
if text == "int":
    data = int(input())
elif text == "real":
    data = float(input())
elif text == "string":
    data = input()

def action(a,b):
    global result
    if a == "int":
        result = (int(b) * 2)
    elif a == "real":
        c = b*1.5
        result = ("%.2f"%c)
    elif a == "string":
        result = ("$"+b+"$")
    return result

print(action(text,data))