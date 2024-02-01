# https://leetcode.com/problems/missing-ranges/


def find_missing_ranges(nums, lower, upper):
    if not nums: return[[lower, upper]]
    results = []
    if lower < nums[0]:
        results.append([lower, nums[0] - 1])

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] <= 1: continue
        results.append([nums[i] + 1, nums[i + 1] - 1])

    if upper > nums[-1]:
        results.append([nums[-1] + 1, upper])
    return results

assert find_missing_ranges([0,1,3,50,75], 0, 99) == [[2,2],[4,49],[51,74],[76,99]]

assert find_missing_ranges([-1], -1, -1) == []

assert find_missing_ranges([], 1, 8) == [[1,8]]
