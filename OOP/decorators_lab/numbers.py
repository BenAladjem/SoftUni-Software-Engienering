# def number_increment(nums):
#     def increase():
#         return [x + 1 for x in nums]
#     return increase()
#
#
#
# print(number_increment([1, 2, 3, 4]))

# def sort_nums(nums):
#     def even():
#         ev = [x for x in nums() if x % 2 == 0]
#         return ev
#     return even
from decorators_exercise.sor_num import sort_nums

@sort_nums
def pr_num():
    return [1, 2, 3, 4, 5, 6, 7]


print(pr_num())
