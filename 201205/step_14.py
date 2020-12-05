group_28 = [
    ['Данила', '5', '4', '5', '3', '4', '2'],
    ['Илья', '2', '3', '3', '4', '5', '5', '5'],
    ['Георгий', '5', '5', '4', '5', '3', '4'],
    ['Соня', '4', '4', '3', '5', '5', '4', '5'],
    ['Никита', '4', '3', '5', '3', '4', '4'],
    ['Владислав', '4', '3', '4', '5', '4']
]


def show_student(student_record):
    marks = student_record[1:]
    marks_as_int = map(int, marks)
    # print(*marks_as_int)
    marks_avg = sum(marks_as_int) / len(marks)
    marks_as_str = ', '.join(marks)
    print(f'{student_record[0]}: {marks_as_str}, средний балл {marks_avg}')


for record in group_28:
    show_student(record)

# result = map(show_student, group_28)
# next(result)
# next(result)
# next(result)
# next(result)
# next(result)
# next(result)
# next(result)



# 1.0 -> 1
# 2.0 -> 2
# 3.0 -> 3
#
# '1' -> 1
# '2' -> 2
# '3' -> 3