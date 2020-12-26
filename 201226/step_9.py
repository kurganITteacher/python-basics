with open('data/kpk.kss45.ru_timetable.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# print(content)
# '<a class="at_url" href="/attachments/article/2714/Расписание на 28-31 декабря по группам.xls" target="_blank" title="Скачать этот файл (Расписание на 28-31 декабря по группам.xls)">Расписание на 28-31 декабря по группам.xls</a>'
# ' class="at_url" href="/attachments/article/2714/Расписание на 28-31 декабря по группам.xls" target="_blank" title="Скачать этот файл (Расписание на 28-31 декабря по группам.xls)">Расписание на 28-31 декабря по группам.xls'

content_items = content.split('<a ')
for el in content_items[1:]:
    el = el.split('</a>')
    print(el[0])
    print('-' * 80)
