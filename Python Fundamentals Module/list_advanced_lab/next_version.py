given = input().split(".")
given_in = ["".join((x) for x in given)]
given_int = int(given_in[0]) +1
given_as_str = []
given_as_str.append(given_int)
text = str(given_as_str[0])

#
# for i in range(len(text)):
#     if not i==(len(text)-1):
#         print(f"{text[i]}.",end='')
#     else:
#         print(f"{text[i]}",end='')
print(f'{".".join(text)}')