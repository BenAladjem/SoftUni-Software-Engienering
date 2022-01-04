n = int(input())
name = input()
total_rate = 0
total_pr = 0
while not name=='Finish':
    sum_b = 0
    for i in range (0,n):
        rat = float(input())
        sum_b+=rat
        total_rate+=rat
        total_pr+=1
    print("%s - %.2f."%(name,sum_b/n))
    name=input()
print("Student's final assessment is %.2f."%(total_rate/total_pr))