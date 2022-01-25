import math

students = int(input())
num_lects = int(input())
bonus = int(input())
visit_students = []
for i in range(students):
    visit_students.append(int(input()))

bonus_student = [(x/num_lects)*(5 + bonus) for x in visit_students]
#print(bonus_student)
max_bonus = max(bonus_student)
#posicion = bonus_student.index((max_bonus))
max_lectures = max(visit_students)
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")