lesson_dates = [
    '19.05.15',
    '19.05.17',
    '19.05.18',
    '19.05.19',
    '19.05.22'
]
student_marks = [
    5,
    4,
    3,
    2,
    5
]

# lesson_dates_and_marks = [
#     ['19.05.15', 5],
#     ['19.05.17', 4],
#     ['19.05.18', 3],
#     ['19.05.19', 2],
#     ['19.05.22', 5],
# ]

# for i, mark in enumerate(student_marks):
#     print(lesson_dates[i], 'оценка', mark)

# Union
# for record in lesson_dates_and_marks:
#     lesson_date, mark = record
#     # print(record, 'или', lesson_date, mark)
#     print(lesson_date, 'оценка', mark)


# for lesson_date, mark in lesson_dates_and_marks:
#     print(lesson_date, 'оценка', mark)


for lesson_date, mark in zip(lesson_dates, student_marks):  # ['19.05.15', 5]
    print(lesson_date, 'оценка', mark)
