text = input().split("\\")
name = text[-1].split(".")
print(f"File name: {name[0]}")
print(f"File extension: {name[1]}")