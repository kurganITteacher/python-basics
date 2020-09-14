student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if mark:
        student_marks.append(mark)
    else:
        break

print('ввод завершен')
print(student_marks)

# ['5', '4', '3', '5', '2']
#   0    1    2    3    4
i = 0
avg_mark = 0
while i < len(student_marks):
    # print(type(avg_mark), type(student_marks[i]))
    # avg_mark = avg_mark + int(student_marks[i])
    avg_mark += int(student_marks[i])
    # i = i + 1
    i += 1
# avg_mark = avg_mark / len(student_marks)
avg_mark /= len(student_marks)
print('средний балл', avg_mark)

# <num1> + <num2> - binary operation
# -<num> - unary operation
# 0 + '5' -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
