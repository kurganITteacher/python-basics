# int()
# float()
# list()
# str()

# тех задание

group_28 = ['Данила', 'Илья', 'Георгий', 'Соня', 'Никита', 'Владислав']
group_28_2 = ('Данила', 'Илья', 'Георгий', 'Соня',
              'Никита', 'Владислав')

print(type(group_28), group_28.__sizeof__())  # CD-RW, mutable
print(type(group_28_2), group_28_2.__sizeof__())  # CD-R, immutable
# CD-R VS CD-RW

# mutable: list, dict, set
# immutable: tuple, int, float, str

# for student in group_28:
#     print(student)
