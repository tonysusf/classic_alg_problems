# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    print('nums are', nums, 'target is', target)
    lookup = {}
    result = None
    for i in range(len(nums)):
        if nums[i] in lookup: # found
            result = [lookup[nums[i]], i]
            break
        else:
            lookup[target - nums[i]] = i
    print('result is', result)
    return result

nums = [2, 7, 11, 15]
target = 9
assert(two_sum(nums, target) == [0, 1])

nums = [3, 2, 4]
target = 6
assert(two_sum(nums, target) == [1, 2])

nums = [3, 3]
target = 6
assert(two_sum(nums, target) == [0, 1])

