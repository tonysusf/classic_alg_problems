# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left


def length_of_longest_increase_sub_v1(nums): # runtime O(n^2)
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def length_of_longest_increase_sub_v2(nums): # runtime O(n * log n), space O(n)
    sub = []
    for num in nums:
        # https://docs.python.org/3/library/bisect.html#bisect.bisect_left
        i = bisect_left(sub, num) # binary search

        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)

nums = [10,9,2,5,3,7,101,18]
assert length_of_longest_increase_sub_v2(nums) == 4
assert length_of_longest_increase_sub_v1(nums) == 4

nums = [0,1,0,3,2,3]
assert length_of_longest_increase_sub_v2(nums) == 4
assert length_of_longest_increase_sub_v1(nums) == 4

nums = [7,7,7,7,7,7,7]
assert length_of_longest_increase_sub_v2(nums) == 1
assert length_of_longest_increase_sub_v1(nums) == 1

