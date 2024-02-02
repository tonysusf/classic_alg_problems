# related: https://docs.python.org/3/library/bisect.html#bisect.bisect_left

import bisect

def binary_search(nums, target): # find the value target in the list, return the index
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]: # found
            return mid
        if target < nums[mid]: # target smaller than mid, so move R to left side
            r = mid - 1
        else: # target larger than mid, so move L to the right side
            l = mid + 1
    return None


nums = [1, 3, 5, 7, 9, 11, 13, 15, 17]
assert binary_search(nums, 9) == 4

# built-in binary search
assert bisect.bisect_left(nums, 9) == 4

