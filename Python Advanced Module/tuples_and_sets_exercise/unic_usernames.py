num = int(input())
usernames = set()
for i in range(num):
    username = input()
    usernames.add(username)

for u in usernames:
    print(u)