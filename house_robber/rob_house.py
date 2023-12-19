# https://leetcode.com/problems/house-robber/


def rob(nums):
    if not nums:
        return 0
    rob3 = 0
    rob2 = nums[-1]
    
    for i in range(len(nums)-2, -1, -1): # move backwards
        current = max(rob2, rob3 + nums[i])
        rob2, rob3 = current, rob2
    return rob2


nums = [1,2,3,1]
assert rob(nums) == 4


nums = [2,7,9,3,1]
assert rob(nums) == 12
