# https://leetcode.com/problems/house-robber-ii/

def rob_cicrle(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    a = _rob(nums[:-1]) # no last one
    b = _rob(nums[1:]) # no 1st one
    return max(a, b)

def _rob(nums):
    t1 = t2 = 0
    for current in nums:
        t1, t2 = max(current + t2, t1), t1
    return t1

nums = [2,3,2]
assert rob_cicrle(nums) == 3


nums = [1,2,3,1]
assert rob_cicrle(nums) == 4


nums = [1,2,3]
assert rob_cicrle(nums) == 3