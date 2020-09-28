f = open('nginx_logs_head.txt', 'r', encoding='utf-8')
# print(type(f))
# print(dir(f))

file_data = f.readlines()
# print(file_data)
for row in file_data:
    row = row.strip()
    print(row)
