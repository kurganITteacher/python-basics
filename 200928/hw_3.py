import students_stat

students_log = students_stat.parse_marks('students_log.txt')
students_log_2 = students_stat.parse_marks('students_log_2.txt')

# print(students_log)
# print(students_log_2)

students_stat.show_marks(students_log)
students_stat.save_marks('students_log.csv', students_log)
