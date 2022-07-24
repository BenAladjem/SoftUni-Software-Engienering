
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range (n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(4)
def say_hi():
    print("Hello")

say_hi()