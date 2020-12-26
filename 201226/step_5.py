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
    el = el.lower().strip('«».,?!…<>[]()-—+*^:;\'"')
    if not el:
        continue
    if el not in text_items_counter:
        text_items_counter[el] = 0
    text_items_counter[el] = text_items_counter[el] + 1

print(f'уникальных слов в тексте {len(text_items_counter)}')
chart_len = 100
text_items_cnt_ordered = dict(sorted(text_items_counter.items(), key=lambda x: x[1], reverse=True)[:chart_len])
print(f'TOP-{len(text_items_cnt_ordered)}')
print(text_items_cnt_ordered)
# https://translate.google.com/?hl=ru&sl=ru&tl=en&text=%D0%BC%D0%B0%D0%BB%D1%8B%D1%88&op=translate
