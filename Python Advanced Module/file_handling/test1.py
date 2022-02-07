file = open('sample.txt', 'x')
print(file.readlines())
# x - creare new file
# w - create new file or overwrite existing
# a - create new file or oppening to existing
try:
    open('file_name', 'r')
    print('File found')
except:
    print('File not found')