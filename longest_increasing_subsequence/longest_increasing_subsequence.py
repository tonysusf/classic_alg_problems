# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left

def length_of_longest_increase_sub(nums):
    sub = []
    for num in nums:
        # https://docs.python.org/3/library/bisect.html#bisect.bisect_left
        i = bisect_left(sub, num)

        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)

nums = [10,9,2,5,3,7,101,18]
assert length_of_longest_increase_sub(nums) == 4

nums = [0,1,0,3,2,3]
assert length_of_longest_increase_sub(nums) == 4

nums = [7,7,7,7,7,7,7]
assert length_of_longest_increase_sub(nums) == 1

