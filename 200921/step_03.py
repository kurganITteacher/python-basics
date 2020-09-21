# legacy code
# python 2.7

student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if not mark:
        break
    if not 48 <= ord(mark) <= 57:
        print('вы ввели не число')
        continue

    mark = int(mark)
    if 1 <= mark <= 5:
        student_marks.append(mark)
    elif mark > 5:
        print("Оценка больше 5")
    elif mark < 1:
        print("Оценка меньше 1")

print('ввод завершен', student_marks)

# if a > b:
#     if b > c:
#         if c > d:
#             pass
#         elif s > k:
#             pass
#     elif t < m:
#         pass
