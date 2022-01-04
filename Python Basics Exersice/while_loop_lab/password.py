username: str = input()
password = input()
data = input()
while data!=password:
    data = input()
else:
    print(f"Welcome {username}!")