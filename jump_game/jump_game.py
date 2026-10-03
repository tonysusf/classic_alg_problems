# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


def can_jump(nums):
    print('input is', nums)
    farthest = 0
    for i, value in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest,i+value)
    return True


nums = [2,3,1,1,4]
assert can_jump(nums) == True


nums = [3,2,1,0,4]
assert can_jump(nums) == False


nums = [3]
assert can_jump(nums) == True

nums = [2, 0, 0, 0]
assert can_jump(nums) == False