# https://leetcode.com/problems/maximum-subarray/


def max_sub_array_sum(nums):
    current = max_sum = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        max_sum = max(max_sum, current)
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
assert max_sub_array_sum(nums) == 6

nums = [1]
assert max_sub_array_sum(nums) == 1

nums = [5,4,-1,7,8]
assert max_sub_array_sum(nums) == 23
