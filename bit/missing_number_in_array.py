# https://leetcode.com/problems/missing-number/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


def find_missing_num_v1(nums): # O(n) runtime, O(n) space
    num_set = set(nums)
    for k in range(len(nums)+1):
        if k not in num_set:
            return k

def find_missing_num_v2(nums): # O(n) runtime, O(1) space
    x = 0
    for i in range(len(nums)):
        x ^= i
        x ^= nums[i]
    x ^= len(nums)
    return x


nums = [3,0,1]
assert find_missing_num_v1(nums) == 2
assert find_missing_num_v2(nums) == 2

nums = [0,1]
assert find_missing_num_v1(nums) == 2
assert find_missing_num_v2(nums) == 2

nums = [9,6,4,2,3,5,7,0,1]
assert find_missing_num_v1(nums) == 8
assert find_missing_num_v2(nums) == 8

