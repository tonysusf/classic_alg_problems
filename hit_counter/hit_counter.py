# https://leetcode.com/problems/design-hit-counter/

from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque() # a double linked list with each item as timestamp and num of hits
        self.total_hits = 0 # storing the total count to avoid a full scan

    def hit(self, timestamp: int) -> None: # O(1)
        if self.hits and self.hits[-1][0] == timestamp: # +1 and put it back
            self.hits[-1][1] += 1
        else: # add a new one
            self.hits.append([timestamp, 1])
        self.total_hits += 1

    def get_hits(self, timestamp: int) -> int: # O(n)
        # remove the ones diff > 300
        while self.hits:
            if timestamp - self.hits[0][0] >= 300:
                self.total_hits -= self.hits[0][1]
                self.hits.popleft()
            else:
                break
        return self.total_hits



hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
assert hc.get_hits(4) == 3

hc.hit(300)
assert hc.get_hits(300) == 4
assert hc.get_hits(301) == 3

