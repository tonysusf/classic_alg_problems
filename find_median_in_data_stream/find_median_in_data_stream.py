# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class Solution:
    def __init__(self):
        # max heap for left, min heap for right part
        self.max_heap = [] # use negative
        self.min_heap = []

    def add_num(self, num):
        # insert into max heaq regardless
        heapq.heappush(self.max_heap, -num)

        # check largest of max heap (left) vs smallest of min heap (right)
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]: # if so move from max to min heap
            tmp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp)

        # rebalance left vs right
        if len(self.max_heap) > len(self.min_heap) + 1:
            tmp = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, tmp)
        elif len(self.min_heap) > len(self.max_heap):
            tmp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0])/2


solution = Solution()
solution.add_num(1)
solution.add_num(2)
assert solution.find_median() == 1.5

solution.add_num(3)
assert solution.find_median() == 2.0
