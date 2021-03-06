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

latest_href = valid_refs[0]
url = f'{ROOT_URL}{latest_href}'
print(f'downloading latest file: {url}')
f_name = latest_href.split('/')[-1]
f_path = os.path.join('data', f_name)
response = requests.get(url, headers=HEADERS, stream=True)
if response.status_code == 200:
    with open(f_path, 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
