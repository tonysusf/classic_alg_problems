# https://leetcode.com/problems/3sum/


def three_sum(nums):
    results = []
    nums.sort()
    print('------input', nums)
    i = 0
    while i < len(nums) and nums[i] <= 0: # up to the zero only
        if i == 0 or nums[i - 1] != nums[i]: # skip duplicate
            _find_two_sum(nums, i, results)
        i += 1
    print('results', results)
    return results

def _find_two_sum(nums, idx, results): # for a given index, find the other 2 nums sum to 0
    lookup = set()
    p = idx + 1
    while p < len(nums): # scan the right part of idx
        target = 0 - nums[idx] - nums[p]
        if target in lookup:
            results.append([nums[idx], nums[p], target])
            while p < len(nums) - 1 and nums[p] == nums[p + 1]: # skip duplicate
                p += 1
        lookup.add(nums[p])
        p += 1

def _to_str(l):
    for row in l:
        row.sort()
        for i in range(len(row)):
            row[i] = str(row[i])
    l = [','.join(k) for k in l]
    l.sort()
    out = '|'.join(l)
    return out


nums = [-1, 0, 1, 2, -1, -4]
results = three_sum(nums)
assert _to_str(results) == _to_str([[-1,-1,2],[-1,0,1]])


nums = [0, 1, 1]
results = three_sum(nums)
assert _to_str(results) == _to_str([[]])


nums = [0, 0, 0]
results = three_sum(nums)
assert _to_str(results) == _to_str([[0,0,0]])

