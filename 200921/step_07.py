# class_pupils = input('введите имена учеников через запятую:\n')
# Полина, Антон, Арсений, Евгений, Алексей, Тимур
# result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']
# assertion
# TDD -> test driven development

class_pupils = 'Полина, Антон, Арсений, Евгений, Алексей, Тимур'
correct_result = ['Полина', 'Антон', 'Арсений', 'Евгений', 'Алексей', 'Тимур']

# print('ученики класса:', class_pupils)
# ...
result = class_pupils.split(', ')

assert result == correct_result, 'алгоритм реализован неверно'
# assert True or False: True -> calm, False -> assertion ERROR

# if not result == correct_result:
#     raise AssertionError('алгоритм реализован неверно')

print(result)
