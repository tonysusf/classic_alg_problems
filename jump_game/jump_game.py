# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


def can_jump(nums):
    memo = []
    memo = ['UNKNOWN'] * len(nums)
    memo[-1] = 'GOOD'
    return can_jump_from_pos(0, nums, memo)

def can_jump_from_pos(p, nums, memo):
    if memo[p] != 'UNKNOWN':
        return memo[p] == 'GOOD'

    furthest_jump = min(p + nums[p], len(nums) - 1)
    for nextPosition in range(p+1, furthest_jump+1):
        if can_jump_from_pos(nextPosition, nums, memo):
            memo[p] = 'GOOD'
            return True
    memo[p] = 'BAD'
    return False


nums = [2,3,1,1,4]
assert can_jump(nums) == True


nums = [3,2,1,0,4]
assert can_jump(nums) == False


nums = [3]
assert can_jump(nums) == True

nums = [2, 0, 0, 0]
assert can_jump(nums) == False