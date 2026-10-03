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

def find_kth_largest_v3(nums, k):
    target = len(nums) - k

    def quickselect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[right] = nums[right], nums[p]

        if p == target:
            return nums[p]
        elif p < target:
            return quickselect(p + 1, right)
        else:
            return quickselect(left, p - 1)

    return quickselect(0, len(nums) - 1)

assert find_kth_largest_v1([3,2,1,5,6,4], 2) == 5
assert find_kth_largest_v2([3,2,1,5,6,4], 2) == 5
assert find_kth_largest_v3([3,2,1,5,6,4], 2) == 5

assert find_kth_largest_v1([3,2,3,1,2,4,5,5,6], 4) == 4
assert find_kth_largest_v2([3,2,3,1,2,4,5,5,6], 4) == 4
assert find_kth_largest_v3([3,2,3,1,2,4,5,5,6], 4) == 4