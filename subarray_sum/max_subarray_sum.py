# https://leetcode.com/problems/maximum-subarray/


def max_sub_array_sum(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
assert max_sub_array_sum(nums) == 6

nums = [1]
assert max_sub_array_sum(nums) == 1


nums = [5,4,-1,7,8]
assert max_sub_array_sum(nums) == 23
