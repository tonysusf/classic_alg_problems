# https://leetcode.com/problems/kth-largest-element-in-an-array/


import heapq


def find_kth_largest_v1(nums, k):
    topk = heapq.nlargest(k, nums)
    return topk[-1]


def find_kth_largest_v2(nums, k):
    min_heap = [] # use a k sized min heap to track the k largest numbers
    for x in nums:
        heapq.heappush(min_heap, x)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

assert find_kth_largest_v1([3,2,1,5,6,4], 2) == 5
assert find_kth_largest_v2([3,2,1,5,6,4], 2) == 5

assert find_kth_largest_v1([3,2,3,1,2,4,5,5,6], 4) == 4
assert find_kth_largest_v2([3,2,3,1,2,4,5,5,6], 4) == 4
