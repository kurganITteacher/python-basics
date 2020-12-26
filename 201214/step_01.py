def show_user(user):
    print('имя:', user[0])
    print('фамилия:', user[2])
    print('возраст:', user[3])


user_1 = ['Иван', 'Иванович', 'Иванов', 21, 'г.Курган']
#           0          1          2      3       4
user_2 = ['Петр', 'Петрович', 'Петров', 19, 'г.Далматово']
user_3 = ['Сидорова', 'Валерьевна', 'Оксана', 23, 'г.Шадринск']

# show_user(user_1)
# show_user(user_2)
# show_user(user_3)

for el in user_1:
    print(el)
