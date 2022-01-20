text = input()

encr_list = [chr(ord(x)+3) for x in text]
print("".join(encr_list))