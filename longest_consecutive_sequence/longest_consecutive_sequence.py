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


nums = [100,4,200,1,3,2]
assert longest_consecutive(nums) == 4

nums = [0,3,7,2,5,8,4,6,0,1]
assert longest_consecutive(nums) == 9

nums = [0,3, 1, 2, 9]
assert longest_consecutive(nums) == 4

