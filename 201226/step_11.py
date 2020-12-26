import os
import shutil

import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}
ROOT_URL = 'https://kpk.kss45.ru'

with open('data/kpk.kss45.ru_timetable.txt', 'r', encoding='utf-8') as f:
    content = f.read()

content_items = content.split('<a ')
valid_refs = []
for el in content_items[1:]:
    ref_content = el.split('</a>')[0]
    if 'Расписание' not in ref_content or '.xls' not in ref_content:
        continue
    clean_ref_content = ref_content.split('href="')[1].split('"')[0]
    valid_refs.append(clean_ref_content)

print(f'valid references {len(valid_refs)}')
# print(*valid_refs, sep='\n\n')

for href in valid_refs:
    url = f'{ROOT_URL}{href}'
    # https://kpk.kss45.ru/attachments/article/2608/Расписание на 26-31 октября по аудиториям.xls
    f_name = href.split('/')[-1]
    f_path = os.path.join('data', 'timetables', f_name)
    # print(f_path)
    response = requests.get(url, headers=HEADERS, stream=True)
    if response.status_code == 200:
        with open(f_path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
