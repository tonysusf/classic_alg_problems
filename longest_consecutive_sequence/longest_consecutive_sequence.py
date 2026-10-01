# https://leetcode.com/problems/longest-consecutive-sequence/

def longest_consecutive(nums):
    max_len = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_len = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_len += 1

            max_len = max(max_len, current_len)

    return max_len


assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

assert longest_consecutive([0, 3, 1, 2, 9]) == 4

assert longest_consecutive([]) == 0

assert longest_consecutive([5]) == 1

assert longest_consecutive([1, 2]) == 2

assert longest_consecutive([10, 30, 50]) == 1

assert longest_consecutive([1, 2, 3, 4, 5]) == 5

assert longest_consecutive([5, 4, 3, 2, 1]) == 5

assert longest_consecutive([-3, -2, -1, 0, 1]) == 5

assert longest_consecutive([-2, -1, 1, 2, 3, 0]) == 6

assert longest_consecutive([1, 2, 2, 3, 3, 3, 4]) == 4

assert longest_consecutive([1, 2, 10, 11, 12, 13, 20]) == 4

assert longest_consecutive([1000, -1000, 5]) == 1
