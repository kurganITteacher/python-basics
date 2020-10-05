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
            result.append([last_name, first_name, patronymic, marks, avg_mark])
            # result.append(
            #     {
            #         'last_name': last_name,
            #         'first_name': first_name,
            #         'patronymic': patronymic,
            #         'marks': marks,
            #         'avg_mark': avg_mark
            #     }
            # )
    return result


def show_marks(parsed_marks, raw=True, sep=' '):
    for row in parsed_marks:
        if raw:
            print(row)
        else:
            print(sep.join(map(str, row)))


def save_marks(f_name, parsed_marks):
    head = ['last_name', 'first_name', 'patronymic', 'marks', 'avg_mark']
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(', '.join(head))
        f.write('\n')
        for row in parsed_marks:
            f.write(', '.join(map(str, row)))
            f.write('\n')
