# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    print('-----input:', nums, target)
    lookup = {}
    result = None
    for i in range(len(nums)):
        if nums[i] in lookup: # found
            result = [lookup[nums[i]], i]
            break
        else:
            lookup[target - nums[i]] = i
    print('result=', result)
    return result

nums = [2, 7, 11, 15]
target = 9
assert(two_sum(nums, target) == [0, 1])
