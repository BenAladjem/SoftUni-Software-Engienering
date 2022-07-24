
def uppercase(func):
    def wrapper():
        result = func()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


@uppercase
def speak():
    return "hello, a am speaking"

print(speak())
