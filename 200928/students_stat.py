def parse_marks(f_name):
    result = []
    with open(f_name, 'r', encoding='utf-8') as f:
        for row in f.read().splitlines():
            last_name, first_name, patronymic, row_marks = row.split(maxsplit=3)
            patronymic = patronymic.strip(',')
            marks = []
            for mark in row_marks.split(','):
                marks.append(int(mark.strip()))
            avg_mark = sum(marks) / len(marks)
            # print(last_name, first_name, patronymic, ':', marks, ', средний балл', avg_mark)
            # result.append([last_name, first_name, patronymic, ':', marks, ', средний балл', avg_mark])
            result.append([last_name, first_name, patronymic, marks, avg_mark])
    return result


def show_marks(parsed_marks):
    for row in parsed_marks:
        # print(row)
        print(' '.join(map(str, row)))


def save_marks(f_name, parsed_marks):
    with open(f_name, 'w', encoding='utf-8') as f:
        for row in parsed_marks:
            f.write(', '.join(map(str, row)))
            f.write('\n')

