student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if mark:
        student_marks.append(mark)
    else:
        break

print('ввод завершен')
print(student_marks)
