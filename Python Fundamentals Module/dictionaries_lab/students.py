data = input()
courses = {}

while ":" in data:
    student_name, id, course_name = data.split(":")