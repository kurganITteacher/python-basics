with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
        patronymic = patronymic.strip(',')
        # marks = list(map(int, map(str.strip, row_marks.split(','))))
        # ' 5' -> map str.strip(' 5') -> '5' -> map int('5') -> 5
        # map(callback_1, iterable)
        # map(callback_2, map(callback_1, iterable))
        # map(callback_3, map(callback_2, map(callback_1, src_iterable)))
        marks = []
        for mark in row_marks.split(','):
            marks.append(int(mark.strip()))
        avg_mark = sum(marks) / len(marks)
        print(last_name, first_name, patronymic, ':', marks, ', средний балл', avg_mark)
