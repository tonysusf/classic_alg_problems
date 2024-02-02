# https://leetcode.com/problems/random-pick-index/

from collections import defaultdict
import random

class Solution:
    def __init__(self, nums):
        self.lookup = defaultdict(list)
        for i in range(len(nums)):
            self.lookup[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return self.lookup[target][random.randint(0, len(self.lookup[target])-1)]


s = Solution([1, 2, 3, 3, 3])
assert s.pick(3) in [2, 3, 4]

