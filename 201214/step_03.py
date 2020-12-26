user_1 = {
    'first_name': 'Иван',
    'patronymic': 'Иванович',
    'last_name': 'Иванов',
    'age': 21,
    'address': 'г.Курган'
}
user_2 = {
    'first_name': 'Петр',
    'patronymic': 'Петрович',
    'last_name': 'Петров',
    'age': 19,
    'address': 'г.Далматово'
}
user_3 = {
    'last_name': 'Сидорова',
    'patronymic': 'Валерьевна',
    'first_name': 'Оксана',
    'age': 23,
    'address': 'г.Шадринск'
}

# for el in user_1:  # only keys
#     print(el)

# for el in user_1.items():  # call the dict method .items()
#     print(el)

for key, val in user_1.items():  # call the dict method .items()
    print(key, val, sep=', ')

# a = 15
# b = 'hello'
# print(a, b)
# a, b = b, a
# print(a, b)
#
# c = (a, b)  # tuple: immutable list
# print(c)
