# say = 'всем привет!'
say = 'вСеМ пРивЕт!'
print(say)
# print(dir(say))
print(say.islower())
print(say.isupper())

say_2 = say.upper()
print(say_2)

# say_3 = say_2.capitalize()
say_3 = say.capitalize()
print(say_3)

if say.endswith('!'):
    print('эмоционально сказано')

home_task = '''
1. Добавить к алгоритму вычисления среднего балла проверку, 
чтобы оценка была в диапазоне от 1 до 5.
2. Вывести оценки студентов за конкретную дату.
3. Изучить методы строк в Python. Написать пару примеров использования.
PS: файлы с ДЗ в репозитории: hometask_200914_01.py, hometask_200914_02.py
'''
