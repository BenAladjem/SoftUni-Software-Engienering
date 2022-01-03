num = float(input())
in_metr = input()
out_metr = input()
if in_metr=='m':
    if out_metr=='mm':
        num*=1000
    else:
        num*=100
elif in_metr=='cm':
    if out_metr=='m':
        num*=0.01
    else:
        num*=10
else:
    if out_metr=='m':
        num*=0.001
    else:
        num*=0.1
print('%.3f'%(num))