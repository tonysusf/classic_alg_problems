# https://leetcode.com/problems/permutations/description/

def permutate(nums):
    results = []
    _permutate(nums, 0, results)
    return results

def _permutate(nums, p, results):
    if p == len(nums) - 1:
        results.append(nums.copy())
        return
    for idx in range(p, len(nums)):
        nums[p], nums[idx] = nums[idx], nums[p]
        _permutate(nums, p+1, results)
        nums[idx], nums[p] = nums[p], nums[idx]

def _to_set(l):
    return set(['|'.join(str(k)) for k in l])

nums = [1,2,3]
expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
results = permutate(nums)
assert _to_set(results) == _to_set(expected)


nums = [1]
expected = [[1]]
results = permutate(nums)
assert _to_set(results) == _to_set(expected)


