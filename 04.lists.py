lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22'
]
student_marks = [5, 4, 3, 2, 5]

# i = 0
# while i < len(student_marks):
#     print(lesson_dates[i], 'оценка', student_marks[i])
#     i += 1

# for item in student_marks:  # item
#     print('оценка', item)
#
# for item in enumerate(student_marks):  # pairs -> (num, item)
#     print('оценка', item)

for item in enumerate(student_marks):  # pairs -> (num, item)
    i, mark = item
    print('оценка', item, 'или', i, mark)

# user_full_name = ['Иван', 'Иванов']
# # first_name = user_full_name[0]
# # second_name = user_full_name[1]
#
# # first_name, second_name = ['Иван', 'Иванов']
# first_name, second_name = user_full_name
#
# print(first_name, second_name)
#
# a, b, c, d, e = [15, 45, 87, 96, 4]
# print(a, b, c, d, e)


# feature
# in place
for i, mark in enumerate(student_marks):  # pairs -> (num, mark)
    print('оценка', i, mark)
    # print(lesson_dates[i], 'оценка', item)

# i, mark = item -> i, mark = (0, 5) -> i = 0, mark = 5
