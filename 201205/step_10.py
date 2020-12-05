def show_student(group, student):
    print('Студент группы', group, ':', student)


def show_group(group, students):
    for student in students:
        show_student(group, student)


group_28 = ['Данила', 'Илья', 'Георгий', 'Соня', 'Никита', 'Владислав']
show_group('28', group_28)

group_38 = ['Иван', 'Ольга', 'Петр']
show_group('38', group_38)
