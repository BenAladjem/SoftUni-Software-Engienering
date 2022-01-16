text = input()
while not text == "end":
    rev_text = text[::-1]
    print(f"{text} = {rev_text}")

    text = input()