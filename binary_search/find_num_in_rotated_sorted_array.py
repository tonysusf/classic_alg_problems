# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        # left sub array of mid is sorted
        if nums[mid] >= nums[l]:
            if nums[l] <= target < nums[mid]: # binary search move
                r = mid - 1
            else:
                l = mid + 1

        # right sub array of mid is sorted
        else:
            if nums[mid] < target <= nums[r]: # binary search move
                l = mid + 1
            else:
                r = mid - 1
    return -1


nums = [4,5,6,7,0,1,2]
target = 0
assert search(nums, target) == 4

nums = [4,5,6,7,0,1,2]
target = 5
assert search(nums, target) == 1

nums = [4,5,6,7,0,1,2]
target = 7
assert search(nums, target) == 3

nums = [4,5,6,7,0,1,2]
target = 3
assert search(nums, target) == -1

nums = [4,5]
target = 99
assert search(nums, target) == -1
