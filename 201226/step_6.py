import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

url = 'https://translate.google.com/?hl=ru&sl=ru&tl=en&text=%D0%BC%D0%B0%D0%BB%D1%8B%D1%88&op=translate'

# https://www.translated.net/hts/?f=quote&cid=htsdemo&p=htsdemo5&s=english&t=italian&w=1000&of=json
# https://www.translated.net/hts/?f=quote&cid=htsdemo&p=htsdemo5&s=russian&t=english&w=1000&of=json

response = requests.get(url, headers=headers)
content = response.content.decode('utf-8')
print(content)
