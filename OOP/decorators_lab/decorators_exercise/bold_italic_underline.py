
def make_bold(b):
    def wrapper(*args):
        result = b(*args)
        return f"<b>{result}<b>"
    return wrapper


def make_italic(b):
    def wrapper(*args):
        result = b(*args)
        return f"<i>{result}<i>"

    return wrapper

def make_underline(b):
    def wrapper(*args):
        result = b(*args)
        return f"<u>{result}<u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))