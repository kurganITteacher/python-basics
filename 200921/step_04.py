student_marks = []
while True:
    mark = input('введите оценку студента:\n')
    if not mark:
        break
    if len(mark) != 1:
        print('вы ввели не один символ')
        continue
    # if not 48 <= ord(mark) <= 57:
    #     print('вы ввели не число')
    #     continue

    try:
        mark = int(mark)
        if 1 <= mark <= 5:
            student_marks.append(mark)
        elif mark > 5:
            print("Оценка больше 5")
        elif mark < 1:
            print("Оценка меньше 1")
    except TypeError as e:
        print('ошибка типа:', e)
    except ValueError as e:
        print('ошибка значения:', e)
    except AttributeError as e:
        print('ошибка атрибута:', e)
    except ZeroDivisionError as e:
        print('ошибка деления на ноль:', e)
    except Exception as e:
        print('была допущена какая-то ошибка:', e)

print('ввод завершен', student_marks)
