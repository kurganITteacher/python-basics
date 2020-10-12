nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # time complexity O(n)
# for i in range(len(nums)):
#     current = nums[i]
#     print(current)
pass
# time complexity O(n^2)
for i in range(len(nums)):  # n times
    current = nums[i]
    for j in range(i + 1):  # runs form 1 to n
        print(nums[j], end=' | ')
    print()
# n^2 / 2 = 0.5 * n^2 -> n^2

# 10 -> 50 -> 100
# 100 -> 5 000 -> 10 000
