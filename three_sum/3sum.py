# https://leetcode.com/problems/3sum/
# given an array find all triplets sum to 0, no duplicates

def three_sum(nums): # runtime O(n^2), space O(n)
    results = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]: # no dup with last one
            seen = set()
            j = i + 1
            while j < len(nums):
                if -nums[i] - nums[j] in seen:
                    results.append([nums[i], nums[j], -nums[i] - nums[j]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]: # no dup with next one
                        j += 1
                seen.add(nums[j])
                j += 1
    return results


def _to_str(l):
    tmp_l = []
    for row in l:
        row.sort()
        tmp_l.append(','.join([str(k) for k in row]))
    tmp_l.sort()
    return '|'.join(tmp_l)


nums = [-1, 0, 1, 2, -1, -4]
results = three_sum(nums)
assert _to_str(results) == _to_str([[-1,-1,2],[-1,0,1]])

nums = [0, 1, 1]
results = three_sum(nums)
assert _to_str(results) == _to_str([[]])

nums = [0, 0, 0]
results = three_sum(nums)
assert _to_str(results) == _to_str([[0,0,0]])

nums = [0, 0, 0, 0]
results = three_sum(nums)
assert _to_str(results) == _to_str([[0,0,0]])

nums = [0, 0, 0, 0, 0]
results = three_sum(nums)
assert _to_str(results) == _to_str([[0,0,0]])