hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())
time_exam = hour_exam*60+min_exam
time_arrive = hour_arrive*60+min_arrive
delta = abs(time_arrive-time_exam)
delta_h = delta//60
delta_min = delta%60
if time_arrive > time_exam:
    print("Late")
    if delta < 60:
        print(f"{delta_min} minutes after the start")
    else:
        print(f"{delta_h}:{delta_min:0>2d} hours after the start")
elif time_exam-time_arrive >30:
    print("Early")
else:
    print("On time")
if time_arrive <time_exam:
    if delta <60:
        print(f"{delta_min} minutes before the start")
    else:
        print(f"{delta_h}:{delta_min:0>2d} hours before the start")
