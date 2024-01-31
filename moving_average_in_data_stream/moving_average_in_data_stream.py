# https://leetcode.com/problems/moving-average-from-data-stream/

from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.queue_size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, num):
        self.count += 1
        self.queue.append(num)
        tail = self.queue.popleft() if self.count > self.queue_size else 0
        self.window_sum = self.window_sum - tail + num
        return self.window_sum / min(self.queue_size, self.count)



solution = MovingAverage(3)
assert solution.next(1) == 1.0
assert solution.next(10) == 5.5
assert solution.next(3) == 14/3
assert solution.next(5) == 6

