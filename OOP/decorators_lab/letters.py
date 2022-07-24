def vowel_filter(func):
    def wrapper():
        letters = func()
        return [el for el in letters if el.lower() in "aeoui"]
    return wrapper

#from decorators_exercise.sor_num import vowel_filter

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())