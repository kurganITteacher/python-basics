f = open('text_1.txt', 'r', encoding='utf-8')

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

line = f.readline()
while line:
    print(line)
    line = f.readline()

f.close()
