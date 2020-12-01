group_28 = ['Данила', 'Илья', 'Георгий', 'Соня', 'Никита', 'Владислав']
#               0        1        2                            ?
#                                          -3        -2         -1          0

# print(group_28[2])  # hardcode
# len(group_28) -> 6

print(group_28[len(group_28) - 1])  # not ok
print(group_28[-1])  # ok

print(group_28[-4])
print(group_28[len(group_28) - 4])

group_28.append('Петр')  # stack
print(group_28)

group_28.insert(2, 'Роман')
print(group_28)

last_student = group_28.pop()
print(last_student)
print(group_28)

last_student = group_28.pop()
print(last_student)
print(group_28)


