# https://leetcode.com/problems/3sum/
# given an array find all triplets sum to 0, no duplicates

def three_sum(nums): # runtime O(n^2), space O(n)
    results = []
    nums.sort() # sort it 1st!
    print('nums', nums)
    for idx1 in range(len(nums)):
        if nums[idx1] > 0: # scan up to zero
            break
        if idx1 > 0 and nums[idx1 - 1] == nums[idx1]: # skip duplicate
            continue

        # find the other 2 nums after current index summing to 0
        lookup = set()
        for idx2 in range(idx1+1, len(nums)): # scan the right part of idx
            target = 0 - nums[idx1] - nums[idx2]
            if target in lookup:
                results.append([nums[idx1], nums[idx2], target]) # found it
                while idx2 < len(nums) - 1 and nums[idx2] == nums[idx2 + 1]: # skip duplicate
                    idx2 += 1
            else:
                lookup.add(nums[idx2])
    print('results', results)
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


