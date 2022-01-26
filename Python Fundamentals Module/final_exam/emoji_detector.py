import re

pattern = r"(?P<surr>\:\:|\*\*)(?P<emoji>[A_Z][a-z](2,))(?P=surr)"
pattern_number = r"\d"

text = input()
all_nums = re.findall(pattern_number, text)
all_nums_as_integer = [int(num) for num in all_nums]

threshold = 1
for el in all_nums_as_integer:
    threshold *= el


emoji_count = 0
for match in re.finditer(pattern,text):
    emoji_count+=1
    data = match.groupdict()
    emoji = data["emoji"]
    emoji_coolnes = sum([ord(letter) for letter in emoji])


#https://pastebin.com/ED0Xs7Zm

#Задачите за днес: Първо. http://prntscr.com/1j2qa5v\
# Второ. http://prntscr.com/1j2qkzo\
# Директен линк: https://judge.softuni.bg/Contests/2302/05-Programming-Fundamentals-Final-Exam
