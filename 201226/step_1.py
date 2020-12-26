# with open()
# f = open('data/fairy_tale_1.txt', 'r', None, 'utf-8')
# f = open(file='data/fairy_tale_1.txt', mode='r', encoding='utf-8')
# f = open(mode='r', file='data/fairy_tale_1.txt', encoding='utf-8')
# f = open('data/fairy_tale_1.txt', 'r', encoding='utf-8')

# Ф      И    О
# Иванов Иван Иванович
# key  value
# Имя: Иван
# Фамилия: Иванов
# Отчество: Иванович
# kwargs -> keyword args

# Отчество: Иванович
# Фамилия: Иванов
# Имя: Иван

# Ф      И    О
# Иван Иванов Иванович

# f = open('data/fairy_tale_1.txt', 'r', encoding='utf-8')
# content = f.read()
# f.close()

# context managers
with open('data/fairy_tale_1.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# print(content)

# agile
# task -> 6 hours, 1d 8h ->
pass
# task 1 -> найти в тексте уникальные слова и подсчитать их количество
# task 2 -> отсортировать слова в тексте по частоте их появления
# task 3 -> найти перевод для TOP-100

text_items = content.split()
text_items_cnt = len(text_items)
# print('слов в тексте', text_items_cnt)
print(f'слов в тексте {text_items_cnt}')  # python 3.6+

text_items_counter = {}
for el in text_items:
    el = el.lower()
    if el not in text_items_counter:
        text_items_counter[el] = 0
    text_items_counter[el] = text_items_counter[el] + 1
    # text_items_counter[el] += 1

# el='Теперь'
# {
#     'какой': 5,
#     'её': 1,
#     'Теперь': 4,
# }

print(f'уникальных слов в тексте {len(text_items_counter)}')
