# Кормен Алгоритмы. Вводный курс.

group_28 = ['Данила', 'Илья', 'Георгий', 'Соня', 'Никита', 'Владислав']
#            0         1        2           3       4          5

# group_28.pop()  # O(1)
# group_28 = ['Данила', 'Илья', 'Георгий', 'Соня', 'Никита']
# #            0         1        2           3       4


# group_28.pop(1)  # n=6, O(n) -> O(4)
# group_28 = ['Данила', 'Георгий', 'Соня', 'Никита', 'Владислав']
# #            0           1          2        3         4

# group_28.insert(1, 'Петр')  # O(1) VS !O(n)! VS O(n^2) VS O(log(n))...
# print(group_28)
# O(n^2) -> O(n)

# O(n): 3 ms -> 1000 -> 3000 -> 3s
# O(n^2): 3 ms -> 1000^2 = 1 000 000 -> 3 000 000 -> 3000s -> 50 min
