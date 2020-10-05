import random

import students_stat

students_stat.parse_marks('students_log.txt')
students_stat.parse_marks('students_log_2.txt')
# DRY

print(random.choice([51, 68, 47, 69, 12, 35]))
