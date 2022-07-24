
def even_parameters(a):
    def wrapper(*args):
        for ar in args:
            try:
                if not ar % 2 == 0:
                    return "Please use only even numbers!"
            except:
                return "Please use only even numbers!"
        return a(*args)
    return wrapper






@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))