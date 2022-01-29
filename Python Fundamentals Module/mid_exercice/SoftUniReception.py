first_staff = int(input())
second_staff = int(input())
third_staff = int(input())
num_students = int(input())
n = num_students
stafs_work_hour = first_staff+second_staff+third_staff
h_count = 0
while n > 0:
    h_count+=1
    n -= stafs_work_hour
    if h_count%4==0:
        h_count+=1

print(f"Time needed: {h_count}h.")