# https://leetcode.com/problems/combination-sum/
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

def find_comb_sum(target, current, p, nums, results):
    if target < 0:
        return

    if target == 0:
        results.append(current.copy())
        return

    for i in range(p, len(nums)):
        current.append(nums[i])
        find_comb_sum(target - nums[i], current, i, nums, results)
        current.pop()

def combination_sum(nums, target):
    print(nums, target)
    results = []
    find_comb_sum(target, [], 0, nums, results)
    print(results)
    return results

def _to_str(l):
    for row in l:
        row.sort()
        for i in range(len(row)):
            row[i] = str(row[i])
    l = [','.join(k) for k in l]
    l.sort()
    out = '|'.join(l)
    return out


nums = [2,3,6,7]
target = 7
assert _to_str(combination_sum(nums, target)) == _to_str([[2,2,3],[7]])


nums = [2,3,5]
target = 8
assert _to_str(combination_sum(nums, target)) == _to_str([[2,2,2,2],[2,3,3],[3,5]])


nums = [5]
target = 2
assert _to_str(combination_sum(nums, target)) == ''
