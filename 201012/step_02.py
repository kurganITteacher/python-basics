# range(n) -> 0, 1, 2, n-1, [0, n)
numbers = []
for num in range(10):
    numbers.append(num)
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  0  1  2  3  4  5  6  7  8  9
pass
# Pop last O(1)
# last_num = numbers.pop()  # like cut in word
# # numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
#               0  1  2  3  4  5  6  7  8  remains the same
# # last_num -> 9
# print(numbers)
# print(last_num)
pass
# first_num = numbers.pop(0)
# # Pop intermediate[2] O(n)
# # numbers -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #             0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# # first_num -> 0
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #  1, 2, 3, 4, 5, 6, 7, 8, 9
# #  0, 1, 2, 3, 4, 5, 6, 7, 8
# print(numbers)
# print(first_num)
# # one action -> 9 actions
# # n-elements -> n actions -> big O notation

# some_num = numbers.pop(5)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# #  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# # [0, 1, 2, 3, 4, 6, 7, 8, 9]
#                  #6, 7, 8, 9
# #  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# #  0, 1, 2, 3, 4, 6, 7, 8, 9
# # O(4 + 1) = O(5) -> O(n) -> O(10)
# print(numbers)
# print(some_num)
pass
print(5 in numbers)  # real case O(6) -> O(n)
print(9 in numbers)  # real case O(10) -> O(n)
print(5.5 in numbers)  # real case O(10) -> O(n)
print(0 in numbers)  # real case O(1) -> O(n)

