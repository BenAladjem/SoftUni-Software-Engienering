num = int(input())
def loading(a):
    print(str(a)+"% ["+"%"*(a//10)+"."*(10-a//10)+"]")
    print("Still loading...")
def complete():
    print("100% Complete!")
    print("[%%%%%%%%%%]")
if num==100:
    complete()
else:
    loading(num)