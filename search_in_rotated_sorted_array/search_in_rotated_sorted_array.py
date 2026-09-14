# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Search in Rotated Sorted Array

def search(nums: list[int], target: int) -> int:
    print('input is', nums, 'target is', target)
    l = 0 #left
    r = len(nums) - 1 # right

    while l <= r:
        p = (l + r) // 2 # pivot or mid
        print('checking pivot at', p, 'value is', nums[p])
        if nums[p] == target:
            print('found index', p)
            return p

        if nums[l] <= nums[p]:
            if nums[l] <= target < nums[p]:
                r = p - 1
            else:
                l = p + 1
        else:
            if nums[p] < target <= nums[r]:
                l = p + 1
            else:
                r = p - 1
    return -1


assert search([4,5,6,7,0,1,2], 0) == 4
assert search([4,5,6,7,0,1,2], 3) == -1
assert search([1], 0) == -1
assert search([1], 1) == 0
assert search([5,1,3], 3) == 2
