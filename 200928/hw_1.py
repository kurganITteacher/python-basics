with open('students_log.txt', 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
        patronymic = patronymic.strip(',')
        # marks = list(map(str.strip, row_marks.split(',')))
        marks = []
        for mark in row_marks.split(','):
            marks.append(mark.strip())
        print(last_name, first_name, patronymic, ':', marks)
