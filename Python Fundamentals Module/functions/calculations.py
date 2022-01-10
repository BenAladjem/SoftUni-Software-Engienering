def calculate(operator,num1,num2):
    if operator =="multiply":
        return num1 * num2
    elif operator == "divide":
        return num1//num2
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return  num1 - num2
oper = input()
f_num = int(input())
sec_num = int(input())
print(calculate(oper,f_num,sec_num))