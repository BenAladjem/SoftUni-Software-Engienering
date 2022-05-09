def vowel_filter(func):
    def wrapper():
        letters = func()
        return [let for let in letters if let.lower() in "aeiuo"]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())