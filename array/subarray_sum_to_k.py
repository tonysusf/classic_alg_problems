# https://leetcode.com/problems/subarray-sum-equals-k/

def subarray_sum(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    print('output is', count)
    return count

# 1. Basic case
assert subarray_sum([1, 1, 1], 2) == 2

# 2. Two different subarrays
assert subarray_sum([1, 2, 3], 3) == 2
# [1,2] and [3]

# 3. Negative numbers
assert subarray_sum([1, -1, 0], 0) == 3
# [1,-1], [0], [1,-1,0]

# 4. All zeros
assert subarray_sum([0, 0, 0], 0) == 6

# 5. No matching subarray
assert subarray_sum([1, 2, 3], 10) == 0

# 6. Single element matches
assert subarray_sum([5], 5) == 1

# 7. Single element does not match
assert subarray_sum([5], 3) == 0

# 8. Mixed positive and negative
assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

# 9. Empty input
assert subarray_sum([], 0) == 0
