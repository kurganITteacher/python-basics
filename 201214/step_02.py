def show_user(user):
    print('имя:', user['first_name'])
    print('фамилия:', user['last_name'])
    print('возраст:', user['age'])


# DNS: mega dict -> key - 'domain name': val - 'ip address'
user_1 = {
    'first_name': 'Иван',  # key: value
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

show_user(user_1)
show_user(user_2)
show_user(user_3)
