import requests

response = requests.get('https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/')

print(response)

print(type(response))
# print(dir(response))
print(response.status_code)
print(response.headers)
print(response.content.decode('utf-8'))
