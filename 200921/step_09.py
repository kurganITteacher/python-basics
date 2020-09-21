# class_pupils = input('введите имена учеников через запятую:\n')
# class_pupils = 'Полина,Антон, Арсений , Евгений,  Алексей, Тимур '
class_pupils = 'пОлина,аНТон, арсеНИй , евгЕНИй,  Алексей, тимур '
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

_result = class_pupils.split(',')
result = []
for item in _result:
    # result.append(item.strip().upper())
    # result.append(item.strip().lower().title())
    # result.append(item.strip().capitalize())
    result.append(item.strip().title())


print(result)
assert result == correct_result, 'алгоритм реализован неверно'
