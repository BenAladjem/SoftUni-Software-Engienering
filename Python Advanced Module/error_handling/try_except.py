def raise_exception():
    raise TypeError

def f1():
    try:
        raise_exception()
        return 1
    except ValueError:
        return 2
    finally:
        print('Finally from func')

try:
    print(' -- Try: start')
    raise_exception()
    print(' -- Try: end')
except TypeError:
    print('-- Except')
finally:
    print(' -- Finally')

