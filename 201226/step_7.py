with open('data/fairy_tale_1.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# task 1 -> найти в тексте уникальные слова и подсчитать их количество
# task 2 -> отсортировать слова в тексте по частоте их появления
# task 3 -> найти перевод для TOP-100

text_items = content.split()
text_items_cnt = len(text_items)
print(f'слов в тексте {text_items_cnt}')

short_text_threshold = 3
short_text_items_counter = {}
text_items_counter = {}
for el in text_items:
    el = el.lower().strip('«».,?!…<>[]()-—+*^:;\'"')
    if not el:
        continue
    if len(el) <= short_text_threshold:
        if el not in short_text_items_counter:
            short_text_items_counter[el] = 0
        short_text_items_counter[el] += 1
    else:
        if el not in text_items_counter:
            text_items_counter[el] = 0
        text_items_counter[el] += 1

print(f'уникальных слов / коротких слов в тексте {len(text_items_counter)} / {len(short_text_items_counter)}')
chart_len = 100
text_items_cnt_ordered = dict(
    sorted(text_items_counter.items(), key=lambda x: x[1], reverse=True)[:chart_len]
)
short_text_items_cnt_ordered = dict(
    sorted(short_text_items_counter.items(), key=lambda x: x[1], reverse=True)[:chart_len]
)
print(f'TOP-{len(text_items_cnt_ordered)}')
print(text_items_cnt_ordered)
print(f'\nshort words TOP-{len(text_items_cnt_ordered)}')
print(short_text_items_cnt_ordered)
