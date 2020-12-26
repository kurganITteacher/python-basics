with open('data/fairy_tale_1.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# task 1 -> найти в тексте уникальные слова и подсчитать их количество
# task 2 -> отсортировать слова в тексте по частоте их появления
# task 3 -> найти перевод для TOP-100

text_items = content.split()
text_items_cnt = len(text_items)
print(f'слов в тексте {text_items_cnt}')

text_items_counter = {}
for el in text_items:
    el = el.lower()
    if el not in text_items_counter:
        text_items_counter[el] = 0
    text_items_counter[el] = text_items_counter[el] + 1

print(f'уникальных слов в тексте {len(text_items_counter)}')
# print(text_items_counter)

text_items_cnt_ordered = dict(sorted(text_items_counter.items(), key=lambda x: x[1], reverse=True))
print(text_items_cnt_ordered)

# print(text_items_counter.keys())
# print(text_items_counter.values())
# print(text_items_counter.items())

# for el in text_items_counter.items():
#     print(el)
# 11:05