command = input()
company = ""
id = []
d = {company,id}
while not command == "End":
    info = command.split(" -> ")
    company = (info[0])
    d[company].append(info[1])

    command = input()
print(company)
print(id)

print(d)