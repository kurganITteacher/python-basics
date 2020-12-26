# # «брр-пс-пс»  громче. да…  мумия!  лучше!..»   хи-ти-ти-хи…
# bugs = ['«брр-пс-пс»', 'громче.', 'да…', 'мумия!', 'лучше!..»', 'хи-ти-ти-хи…']
# for item in bugs:
#     print(item, '->', item.strip('«».,?!…'))

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
    # item.strip('«».,?!…')
    el = el.lower().strip('«».,?!…<>[]()-+*^:;\'"')
    if el not in text_items_counter:
        text_items_counter[el] = 0
    text_items_counter[el] = text_items_counter[el] + 1

print(f'уникальных слов в тексте {len(text_items_counter)}')
text_items_cnt_ordered = dict(sorted(text_items_counter.items(), key=lambda x: x[1], reverse=True))
print(text_items_cnt_ordered)

# «брр-пс-пс»  громче. да…  мумия!  лучше!..»   хи-ти-ти-хи…


