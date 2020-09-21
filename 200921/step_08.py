# class_pupils = input('введите имена учеников через запятую:\n')
class_pupils = 'Полина,Антон, Арсений , Евгений,  Алексей, Тимур '
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

_result = class_pupils.split(',')
result = []
for item in _result:
    result.append(item.strip())

assert result == correct_result, 'алгоритм реализован неверно'
