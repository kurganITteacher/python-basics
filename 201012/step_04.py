# n^2 -> n*log(n) or n or log(n)
# n = 100 -> log(100) = 2
# n = 100 000 -> log(100 000) = 5
# x1000 => x2.5

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # real case 10^6
# memory complexity
print(id(nums), nums)
nums.reverse()  # in place -> memory complexity O(1)
print(id(nums), nums)
nums_2 = list(reversed(nums))
print(id(nums_2), nums_2)  # memory complexity O(n)
# memory leaks
