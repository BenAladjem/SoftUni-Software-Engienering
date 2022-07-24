def sort_nums(nums):
    def even():
        ev = [x for x in nums() if x % 2 == 0]
        return ev
    return even

def vowel_filter(func):
    def wrapper():
        letters = func()
        return [el for el in letters if el.lower() in "aeoui"]
    return wrapper