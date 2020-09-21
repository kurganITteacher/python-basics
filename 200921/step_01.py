# False: a='', a=0, a=[]
# https://github.com/PlagueEvgeny/python---basics/blob/master/home_work.py
# refactoring
# dry: Do not Repeat Yourself
# habra-effect -> 404
# bottleneck
# brute force

student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    # mark = int(mark)  # int('') -> exception
    if mark:
        mark = int(mark)  # int('5') -> ok
        # student_marks.append(mark)
        if mark > 5:
            print("Оценка не подходит под категорию оценивания: больше 5")
            # student_marks.remove(mark)  # O(n)
        elif mark < 1:
            print("Оценка не подходит под категорию оценивания: меньше 1")
            # student_marks.remove(mark)  # O(n)
        else:
            student_marks.append(mark)  # O(1)
        # elif int(mark) == 0:
        #     student_marks.remove(int(mark))
    else:
        break

print('ввод завершен')

# 9 mark = '7'
# 11 True
#     student_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2]
# 12 mark = 7
# 13 student_marks = [4, 4, 3, 2, 4, 5, 5, 4, 2, 7]
# 14 True
# 16 student_marks.remove(mark) -> student_marks.remove(7)
# remove() -> search in list (brute force, linear search)
# [4, 4, 3, 2, 4, 5, 5, 4, 2, 7], n = len(student_marks) -> task size, n steps
# [7, 4, 4, 3, 2, 4, 5, 5, 4, 2] -> 1 step, [4, 4, 3, 2, 7, 4, 5, 5, 4, 2] -> n // 2 steps
# list search complexity = O(n)
# O(n) - о большое эн


