# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict

def subarray_sum(nums, k):
    print(nums, k)
    count = 0
    run_sum = 0
    lookup = defaultdict(int)
    lookup[0] = 1 # for checking itself
    for i in range(len(nums)):
        run_sum += nums[i]
        if (run_sum - k) in lookup:
            count += lookup[run_sum - k]
        lookup[run_sum] += 1
    print(count)
    return count


assert subarray_sum([1, 1, 1], 2) == 2

assert subarray_sum([1, 2, 3], 3) == 2

assert subarray_sum([1, -1, 1], 0) == 2

assert subarray_sum([1], 2) == 0

assert subarray_sum([1], 1) == 1

assert subarray_sum([1, -1, -1], -2) == 1