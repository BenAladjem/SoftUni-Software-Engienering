

def type_check(t):
    def check_accept(f):
        def wrapper(arg):
            if type(arg) == t:
                return f(arg)
            else:
                return "Bad Type"
        return wrapper
    return check_accept




@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))