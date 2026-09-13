# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Search in Rotated Sorted Array

def search(nums: list[int], target: int) -> int:
    print("input is", nums, target)
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            print('found it ', mid)
            return mid

        # when the left side is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # when the right side is sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1

assert search([4,5,6,7,0,1,2], 0) == 4
assert search([4,5,6,7,0,1,2], 3) == -1
assert search([1], 0) == -1
assert search([1], 1) == 0
assert search([5,1,3], 3) == 2
