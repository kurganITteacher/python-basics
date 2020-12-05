import requests

response = requests.get('https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-'
                        '%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%'
                        '81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html')

# print(response)

# print(type(response))
# print(dir(response))
# print(response.status_code)
# print(response.headers)
content = response.content.decode('utf-8')
# print(content)
# https://kpk.kss45.ru/attachments/article/2688/%D0%A0%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%B0%207-12%20%D0%B4%D0%B5%D0%BA%D0%B0%D0%B1%D1%80%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D1%80%D0%B5%D0%BF%D0%BE%D0%B4%D0%B0%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%20%D0%9C-%D0%A9.xls
hrefs = content.split('href=')
# print(hrefs)
# print(hrefs[0])

href_1 = hrefs[1].split(' />')[0]
print(href_1)
print('.xls' in href_1)
