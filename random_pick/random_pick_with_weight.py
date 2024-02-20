# https://leetcode.com/problems/random-pick-with-weight/

import random

class Solution:
    def __init__(self, w):
        self.run_sum = [0] * len(w)
        current = 0
        for i in range(len(w)):
            current += w[i]
            self.run_sum[i] = current
        self.total_sum = current

    def pickIndex(self):
        rand = random.randint(1, self.total_sum)
        l = 0
        r = len(self.run_sum) - 1
        while l < r:
            mid = l + (r - l) // 2
            if rand > self.run_sum[mid]:
                l = mid + 1
            else:
                r = mid
        return l


s = Solution([1])
assert s.pickIndex() == 0


s = Solution([1, 3])
assert s.pickIndex() in [0, 1]
assert s.pickIndex() in [0, 1]

